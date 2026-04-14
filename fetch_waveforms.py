#!/usr/bin/env python3
"""
fetch_waveforms.py
==================
Fetch seismic waveforms from the IRIS FDSN web service using ObsPy.

Usage examples
--------------
# Download 10 minutes of BHZ data from IU.ANMO around a known event:
    python fetch_waveforms.py \
        --network IU --station ANMO --location 00 --channel BHZ \
        --starttime 2024-01-01T00:00:00 --duration 600 \
        --filter --plot --output anmo_bhz.mseed

# Download all three broadband components with no filtering:
    python fetch_waveforms.py \
        --network IU --station ANTO --location 00 --channel BH? \
        --starttime 2024-02-06T01:17:00 --duration 600 \
        --plot

# Use a different FDSN data centre (e.g. GEOFON):
    python fetch_waveforms.py \
        --network GE --station WLF --location "" --channel BHZ \
        --starttime 2024-01-01T00:00:00 --duration 300 \
        --service GEOFON --plot
"""

import argparse
import sys

from obspy import UTCDateTime
from obspy.clients.fdsn import Client
from obspy.clients.fdsn.header import FDSNNoDataException, FDSNException


# ---------------------------------------------------------------------------
# Default parameters (can all be overridden from the command line)
# ---------------------------------------------------------------------------
DEFAULTS = dict(
    service="IRIS",
    network="IU",
    station="ANMO",
    location="00",
    channel="BHZ",
    starttime="2024-01-01T00:00:00",
    duration=600,           # seconds
    freqmin=0.1,            # Hz  (bandpass low corner)
    freqmax=10.0,           # Hz  (bandpass high corner)
    output=None,            # path to save MiniSEED file; None = do not save
)


# ---------------------------------------------------------------------------
# Core fetch function
# ---------------------------------------------------------------------------

def fetch_waveforms(
    service: str,
    network: str,
    station: str,
    location: str,
    channel: str,
    starttime: UTCDateTime,
    endtime: UTCDateTime,
) -> "obspy.Stream":
    """
    Connect to an FDSN data centre and download waveform data.

    Parameters
    ----------
    service   : FDSN service identifier recognised by ObsPy, e.g. "IRIS".
    network   : SEED network code, e.g. "IU".
    station   : SEED station code, e.g. "ANMO".
    location  : SEED location code, e.g. "00" or "" for blank.
    channel   : SEED channel code or wildcard, e.g. "BHZ" or "BH?".
    starttime : Start of the requested time window.
    endtime   : End of the requested time window.

    Returns
    -------
    obspy.Stream containing one or more Trace objects.

    Raises
    ------
    SystemExit on network errors or no-data responses.
    """
    print(f"Connecting to {service} FDSN service …")
    client = Client(service)

    # Replace empty-string location with ObsPy's wildcard token
    loc = location if location else "*"

    print(
        f"Requesting  {network}.{station}.{loc}.{channel}  "
        f"{starttime}  →  {endtime}"
    )

    try:
        stream = client.get_waveforms(
            network=network,
            station=station,
            location=loc,
            channel=channel,
            starttime=starttime,
            endtime=endtime,
        )
    except FDSNNoDataException:
        sys.exit(
            "No data available for the requested parameters and time window. "
            "Try a different station or time range."
        )
    except FDSNException as exc:
        sys.exit(f"FDSN error: {exc}")

    print(f"Downloaded {len(stream)} trace(s):")
    print(stream)
    return stream


# ---------------------------------------------------------------------------
# Processing helpers
# ---------------------------------------------------------------------------

def basic_processing(stream, freqmin: float, freqmax: float):
    """
    Apply a standard preprocessing chain to a copy of *stream*:
      1. Merge overlapping/adjacent traces with fill_value=0.
      2. Detrend (remove linear trend).
      3. Taper (5 % cosine taper at each end).
      4. Bandpass filter between *freqmin* and *freqmax* Hz.

    Returns the processed copy; the original is unchanged.
    """
    processed = stream.copy()
    processed.merge(method=1, fill_value=0)
    processed.detrend("demean")
    processed.detrend("linear")
    processed.taper(max_percentage=0.05, type="cosine")
    processed.filter("bandpass", freqmin=freqmin, freqmax=freqmax, corners=4, zerophase=True)
    print(f"Applied bandpass filter: {freqmin} – {freqmax} Hz")
    return processed


def print_stats(stream):
    """Print a short summary table for every trace in the stream."""
    import numpy as np

    print("\n--- Waveform Statistics ---")
    for tr in stream:
        data = tr.data.astype(float)
        print(
            f"  {tr.id:>20s}  |  "
            f"npts={tr.stats.npts:>7d}  "
            f"fs={tr.stats.sampling_rate:>6.2f} Hz  |  "
            f"min={np.min(data):>12.4g}  "
            f"max={np.max(data):>12.4g}  "
            f"rms={np.sqrt(np.mean(data**2)):>12.4g}"
        )
    print()


# ---------------------------------------------------------------------------
# Plotting
# ---------------------------------------------------------------------------

def plot_waveforms(raw_stream, processed_stream=None):
    """
    Plot waveforms.

    If *processed_stream* is provided, show a two-panel comparison
    (raw on top, filtered below).  Otherwise show only the raw traces.
    """
    import matplotlib.pyplot as plt
    import numpy as np

    streams_to_plot = [raw_stream]
    titles = ["Raw waveform"]
    colors = ["steelblue"]

    if processed_stream is not None:
        streams_to_plot.append(processed_stream)
        titles.append("Filtered waveform")
        colors.append("tomato")

    n_traces = len(raw_stream)
    n_panels = len(streams_to_plot)

    fig, axes = plt.subplots(
        n_panels * n_traces, 1,
        figsize=(14, 3.5 * n_panels * n_traces),
        squeeze=False,
    )

    row = 0
    for stream, title_prefix, color in zip(streams_to_plot, titles, colors):
        for tr in stream:
            ax = axes[row, 0]
            times = tr.times()
            ax.plot(times, tr.data, color=color, linewidth=0.6, alpha=0.9)
            ax.set_title(
                f"{title_prefix}  —  {tr.id}  "
                f"({tr.stats.starttime.strftime('%Y-%m-%d %H:%M:%S')} UTC)",
                fontsize=11,
            )
            ax.set_xlabel("Time (s)", fontsize=10)
            ax.set_ylabel("Amplitude", fontsize=10)
            ax.grid(True, alpha=0.3)
            row += 1

    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Fetch seismic waveforms from an FDSN data centre (default: IRIS).",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    # Connection
    p.add_argument("--service", default=DEFAULTS["service"],
                   help="FDSN service name recognised by ObsPy.")

    # SEED codes
    p.add_argument("--network",  "-N", default=DEFAULTS["network"])
    p.add_argument("--station",  "-S", default=DEFAULTS["station"])
    p.add_argument("--location", "-L", default=DEFAULTS["location"])
    p.add_argument("--channel",  "-C", default=DEFAULTS["channel"])

    # Time window
    p.add_argument("--starttime", "-t",
                   default=DEFAULTS["starttime"],
                   help="Start time in ISO-8601 format.")
    p.add_argument("--duration", "-d",
                   type=float, default=DEFAULTS["duration"],
                   metavar="SECONDS",
                   help="Length of the time window in seconds.")

    # Processing
    p.add_argument("--filter", action="store_true",
                   help="Apply bandpass filter to the data.")
    p.add_argument("--freqmin", type=float, default=DEFAULTS["freqmin"],
                   metavar="HZ", help="Bandpass low-corner frequency (Hz).")
    p.add_argument("--freqmax", type=float, default=DEFAULTS["freqmax"],
                   metavar="HZ", help="Bandpass high-corner frequency (Hz).")

    # Output
    p.add_argument("--plot", action="store_true",
                   help="Show an interactive plot of the waveforms.")
    p.add_argument("--output", "-o", default=DEFAULTS["output"],
                   metavar="FILE",
                   help="Save the (processed) stream to a MiniSEED file.")

    return p


def main(argv=None):
    args = build_parser().parse_args(argv)

    # Parse time window
    try:
        starttime = UTCDateTime(args.starttime)
    except Exception as exc:
        sys.exit(f"Invalid --starttime value '{args.starttime}': {exc}")
    endtime = starttime + args.duration

    # Fetch
    raw = fetch_waveforms(
        service=args.service,
        network=args.network,
        station=args.station,
        location=args.location,
        channel=args.channel,
        starttime=starttime,
        endtime=endtime,
    )

    # Process
    processed = None
    if args.filter:
        processed = basic_processing(raw, args.freqmin, args.freqmax)

    # Stats
    print_stats(processed if processed is not None else raw)

    # Save
    stream_to_save = processed if processed is not None else raw
    if args.output:
        stream_to_save.write(args.output, format="MSEED")
        print(f"Saved to {args.output}")

    # Plot
    if args.plot:
        plot_waveforms(raw, processed)

    return stream_to_save


if __name__ == "__main__":
    main()
