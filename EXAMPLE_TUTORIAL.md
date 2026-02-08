# Example 1: Your First Seismology Program

This is a simple, step-by-step tutorial to get you started with seismic data analysis.

## What You'll Learn
- Load seismic data from a data center
- Visualize earthquake waveforms
- Calculate basic seismic parameters
- Use AI to help you code

## Prerequisites
- Completed setup from [SETUP_GUIDE.md](../SETUP_GUIDE.md)
- Google Colab or local Python environment
- Internet connection (to download data)

---

## Step 1: Import Libraries

First, let's import the tools we need:

```python
# Import seismology library
from obspy import UTCDateTime
from obspy.clients.fdsn import Client
import matplotlib.pyplot as plt

# Import numerical tools
import numpy as np

print("✅ All libraries imported successfully!")
```

**💡 AI Tip:** If you get an import error, ask Gemini: "Why am I getting ImportError for obspy?"

---

## Step 2: Connect to Data Center

We'll connect to IRIS, a major seismological data repository:

```python
# Create a client to access IRIS data
client = Client("IRIS")
print("📡 Connected to IRIS data center!")
```

**🤔 What is IRIS?**
IRIS (Incorporated Research Institutions for Seismology) provides access to seismic data from thousands of stations worldwide.

**💡 AI Tip:** Ask NotebookLM: "What is the IRIS data center?"

---

## Step 3: Download Real Earthquake Data

Let's get data from a recent significant earthquake:

```python
# Example: 2024 Turkey-Syria Earthquake
# Define the time window
starttime = UTCDateTime("2024-02-06T01:17:00")  # Earthquake time
endtime = starttime + 600  # Get 10 minutes of data

# Download waveform data
print("⏳ Downloading earthquake data...")

stream = client.get_waveforms(
    network="IU",          # Global Seismographic Network
    station="ANTO",        # Station in Turkey
    location="00",         # Location code
    channel="BHZ",         # Vertical component, broadband
    starttime=starttime,
    endtime=endtime
)

print(f"✅ Downloaded {len(stream)} trace(s)")
print(stream)
```

**📝 Understanding the Parameters:**
- `network`: Organization that operates the station
- `station`: Specific seismometer location (ANTO = Ankara, Turkey)
- `channel`: Type of sensor (BHZ = Broadband, High gain, Vertical)
- `location`: For multiple sensors at same station
- `starttime/endtime`: Time window for data

**💡 AI Tip:** Ask Gemini: "Explain SEED channel codes like BHZ"

---

## Step 4: Visualize the Data

Now let's see what the earthquake looks like:

```python
# Quick plot
stream.plot(size=(800, 400))
```

**🎯 What You See:**
- **X-axis:** Time (seconds or minutes)
- **Y-axis:** Ground motion (counts or velocity)
- **Spikes:** Arrival of different seismic waves

**💡 AI Tip:** Ask: "What do P-waves and S-waves look like on a seismogram?"

---

## Step 5: Get Detailed Information

Let's examine the data more closely:

```python
# Get information about the recording
trace = stream[0]  # First (and only) trace

print(f"\n📊 Data Statistics:")
print(f"Sampling rate: {trace.stats.sampling_rate} Hz")
print(f"Number of samples: {trace.stats.npts}")
print(f"Start time: {trace.stats.starttime}")
print(f"Duration: {trace.stats.endtime - trace.stats.starttime} seconds")
print(f"Station: {trace.stats.station}")
print(f"Channel: {trace.stats.channel}")
```

---

## Step 6: Process the Data

Let's clean up the data by removing noise:

```python
# Make a copy to preserve original
stream_filtered = stream.copy()

# Remove instrument response (convert to velocity)
print("🔧 Removing instrument response...")
stream_filtered.remove_response(output="VEL")

# Apply bandpass filter (keep frequencies between 0.1 and 10 Hz)
print("🔧 Applying bandpass filter...")
stream_filtered.filter("bandpass", freqmin=0.1, freqmax=10.0)

print("✅ Data processed!")
```

**🤔 Why Filter?**
Filters remove unwanted noise and focus on the frequency range where earthquake signals are strongest.

**💡 AI Tip:** Ask: "What is a bandpass filter in seismology?"

---

## Step 7: Compare Raw vs Filtered Data

```python
# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

# Plot raw data
ax1.plot(stream[0].times(), stream[0].data, 'b-', linewidth=0.5)
ax1.set_title('Raw Seismic Data', fontsize=14, fontweight='bold')
ax1.set_xlabel('Time (seconds)')
ax1.set_ylabel('Counts')
ax1.grid(True, alpha=0.3)

# Plot filtered data
ax2.plot(stream_filtered[0].times(), stream_filtered[0].data, 'r-', linewidth=0.5)
ax2.set_title('Filtered Seismic Data', fontsize=14, fontweight='bold')
ax2.set_xlabel('Time (seconds)')
ax2.set_ylabel('Velocity (m/s)')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("📈 Notice how the filtered data shows clearer wave arrivals!")
```

---

## Step 8: Calculate Basic Parameters

Let's extract some useful information:

```python
# Get the data array
data = stream_filtered[0].data

# Calculate statistics
max_amplitude = np.max(np.abs(data))
mean_value = np.mean(data)
std_value = np.std(data)

print(f"\n📊 Waveform Statistics:")
print(f"Maximum amplitude: {max_amplitude:.6f} m/s")
print(f"Mean value: {mean_value:.6f} m/s")
print(f"Standard deviation: {std_value:.6f} m/s")

# Find time of maximum amplitude
max_index = np.argmax(np.abs(data))
max_time = stream_filtered[0].times()[max_index]
print(f"Peak arrival time: {max_time:.2f} seconds after start")
```

---

## Step 9: Identify Wave Arrivals

```python
# Let's zoom in on the first wave arrivals
fig, ax = plt.subplots(figsize=(12, 6))

# Plot first 200 seconds
time = stream_filtered[0].times()
data = stream_filtered[0].data
mask = time <= 200

ax.plot(time[mask], data[mask], 'b-', linewidth=1)
ax.set_title('First 200 Seconds - Wave Arrivals', fontsize=14, fontweight='bold')
ax.set_xlabel('Time (seconds)', fontsize=12)
ax.set_ylabel('Velocity (m/s)', fontsize=12)
ax.grid(True, alpha=0.3)

# Add annotations
ax.axvline(x=50, color='r', linestyle='--', label='Possible P-wave', alpha=0.7)
ax.axvline(x=90, color='g', linestyle='--', label='Possible S-wave', alpha=0.7)
ax.legend()

plt.tight_layout()
plt.show()

print("🌊 P-waves arrive first (faster), S-waves arrive later (slower)")
```

**💡 AI Tip:** Ask: "How can I automatically detect P-wave and S-wave arrivals?"

---

## Step 10: Save Your Work

```python
# Save the processed data
stream_filtered.write("processed_earthquake.mseed", format="MSEED")
print("💾 Saved processed data to 'processed_earthquake.mseed'")

# Save the plot
fig.savefig("earthquake_plot.png", dpi=300, bbox_inches='tight')
print("💾 Saved plot to 'earthquake_plot.png'")
```

---

## 🎉 Congratulations!

You've completed your first seismology program! You've learned to:
- ✅ Connect to seismic data centers
- ✅ Download real earthquake data
- ✅ Visualize seismograms
- ✅ Filter and process seismic signals
- ✅ Calculate basic parameters
- ✅ Identify wave arrivals

---

## 🚀 Next Steps

### Try These Modifications:

1. **Different Station:**
   Change `station="ANTO"` to another station like:
   - `station="ANMO"` (USA)
   - `station="TATO"` (Taiwan)
   - `station="COLA"` (Alaska)

2. **Different Earthquake:**
   Change the `starttime` to analyze other earthquakes:
   ```python
   # 2011 Tohoku Earthquake (Japan)
   starttime = UTCDateTime("2011-03-11T05:46:00")
   
   # 2023 Morocco Earthquake
   starttime = UTCDateTime("2023-09-08T22:11:00")
   ```

3. **Three Components:**
   Download all three components (Vertical, North, East):
   ```python
   # Replace channel="BHZ" with channel="BH*"
   stream = client.get_waveforms(
       network="IU",
       station="ANTO",
       location="00",
       channel="BH*",  # Get all three components
       starttime=starttime,
       endtime=endtime
   )
   ```

### Practice Exercises:

**Exercise 1: Find Local Earthquakes**
- Use the USGS earthquake catalog to find recent events
- Download data from nearby stations
- Compare waveforms from different distances

**Exercise 2: Measure Travel Time**
- Calculate the time difference between P and S waves
- Estimate distance to earthquake
- Compare with actual distance

**Exercise 3: Frequency Analysis**
- Create a spectrogram of the data
- Identify dominant frequencies
- Compare before and after filtering

---

## 🤖 Using AI for Learning

### Good Questions to Ask:

**Conceptual:**
- "Why do P-waves travel faster than S-waves?"
- "What causes surface waves in earthquakes?"
- "How is earthquake magnitude calculated?"

**Technical:**
- "How do I download data from multiple stations?"
- "What's the best filter for regional earthquakes?"
- "How can I convert between different time formats?"

**Debugging:**
- "Why is my stream empty?"
- "How do I fix 'No data available' error?"
- "What does this ObsPy warning mean?"

---

## 📚 Additional Resources

### Recommended Reading:
1. ObsPy Tutorial: https://docs.obspy.org/tutorial/
2. Seismology and the Earth's Interior
3. Introduction to Seismology by Shearer

### Datasets to Explore:
1. Recent earthquakes: https://earthquake.usgs.gov/
2. Continuous data: IRIS DMC
3. Event catalogs: ISC, USGS

### Community:
- ObsPy Users Forum
- Seismology Stack Exchange
- GitHub ObsPy Issues

---

**Happy coding! Remember: The best way to learn is by doing. Try, fail, learn, repeat!** 🌍📊🐍

