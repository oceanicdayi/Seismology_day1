# 📋 Quick Reference Card - Seismology Day 1

**Keep this handy while coding!**

---

## 🚀 Getting Started (Google Colab)

### 1. Setup (Run Once)
```python
!pip install obspy -q
```

### 2. Import Libraries
```python
from obspy import UTCDateTime
from obspy.clients.fdsn import Client
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline
```

### 3. Connect to Data
```python
client = Client("IRIS")
```

---

## 📡 Download Data

### Basic Download
```python
st = client.get_waveforms(
    network="IU",           # Network code
    station="ANMO",         # Station code
    location="00",          # Location code
    channel="BHZ",          # Channel code
    starttime=UTCDateTime("2024-01-01T00:00:00"),
    endtime=UTCDateTime("2024-01-01T01:00:00")
)
```

### Quick Recent Data
```python
t = UTCDateTime() - 86400  # 24 hours ago
st = client.get_waveforms("IU", "ANMO", "00", "BHZ", t, t+3600)
```

### Multiple Components
```python
# Use BH* to get BHZ, BHN, BHE
st = client.get_waveforms("IU", "ANMO", "00", "BH*", t, t+3600)
```

---

## 📊 View & Plot Data

### Quick Look
```python
print(st)              # Show info
st.plot()              # Quick plot
```

### Custom Plot
```python
trace = st[0]
plt.figure(figsize=(12, 4))
plt.plot(trace.times(), trace.data)
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.title(f'{trace.stats.station}.{trace.stats.channel}')
plt.grid(True)
plt.show()
```

---

## 🔧 Process Data

### Filter
```python
# Bandpass filter (keep frequencies between 0.1 and 10 Hz)
st_filtered = st.copy()
st_filtered.filter("bandpass", freqmin=0.1, freqmax=10.0)
```

### Detrend
```python
st.detrend("linear")    # Remove linear trend
st.detrend("demean")    # Remove mean
```

### Resample
```python
st.resample(20.0)       # Resample to 20 Hz
```

---

## 📈 Analysis

### Basic Stats
```python
trace = st[0]
data = trace.data

max_amp = np.max(np.abs(data))
mean = np.mean(data)
std = np.std(data)

print(f"Max: {max_amp}")
print(f"Mean: {mean}")
print(f"Std: {std}")
```

### Find Peak
```python
peak_index = np.argmax(np.abs(data))
peak_time = trace.times()[peak_index]
peak_value = data[peak_index]
print(f"Peak at {peak_time:.2f}s: {peak_value}")
```

---

## 💾 Save Data

### Save Stream
```python
st.write("output.mseed", format="MSEED")
st.write("output.sac", format="SAC")
```

### Save Plot
```python
plt.savefig("plot.png", dpi=300, bbox_inches='tight')
```

---

## 🎯 Common Station Codes

| Code | Location | Type |
|------|----------|------|
| ANMO | New Mexico, USA | Broadband |
| ANTO | Ankara, Turkey | Broadband |
| COLA | Alaska, USA | Broadband |
| TATO | Taiwan | Broadband |
| MBWA | Zimbabwe | Broadband |

---

## 📍 Channel Codes

### Format: [Band][Instrument][Component]

**Band:**
- `B` = Broadband (0.1-10 Hz)
- `H` = High Broadband (10-80 Hz)
- `L` = Long Period (< 0.1 Hz)

**Instrument:**
- `H` = High Gain Seismometer
- `L` = Low Gain Seismometer
- `N` = Accelerometer

**Component:**
- `Z` = Vertical
- `N` = North-South
- `E` = East-West
- `1,2,3` = Orthogonal components

**Examples:**
- `BHZ` = Broadband, High-gain, Vertical
- `HHN` = High-broadband, High-gain, North
- `LHE` = Long-period, High-gain, East

---

## ⏰ Time Formats

### Create Time Objects
```python
# From string
t = UTCDateTime("2024-01-01T12:00:00")

# Current time
t = UTCDateTime()

# Relative time
t = UTCDateTime() - 3600  # 1 hour ago
```

### Time Math
```python
t1 = UTCDateTime("2024-01-01T00:00:00")
t2 = t1 + 3600            # Add 1 hour
diff = t2 - t1            # Difference in seconds
```

---

## 🐛 Common Errors & Fixes

### No Data Available
```python
# Problem: No data for time window
# Fix: Check earthquake time, adjust window
# Try: USGS earthquake catalog for exact times
```

### Import Error
```python
# Problem: No module named 'obspy'
# Fix: Run !pip install obspy
```

### Empty Plot
```python
# Problem: Plot shows nothing
# Fix: Check data is not empty: print(st)
# Add: %matplotlib inline in Colab
```

### Slow Downloads
```python
# Problem: Download takes too long
# Fix: Reduce time window
# Or: Try different client: Client("USGS")
```

---

## 🤖 AI Help Commands

**In Colab:**
- Click 🤖 icon
- Or press `Ctrl + Alt + Enter`

**Good Questions:**
```
"How do I [specific task]?"
"Why is [error message] happening?"
"Explain [concept] in simple terms"
"Debug this code: [paste code]"
```

---

## 🔗 Quick Links

- **IRIS Data**: https://www.iris.edu/
- **USGS Earthquakes**: https://earthquake.usgs.gov/
- **ObsPy Docs**: https://docs.obspy.org/
- **Colab**: https://colab.research.google.com/
- **NotebookLM**: https://notebooklm.google.com/

---

## 📝 Workflow Template

```python
# 1. Setup
from obspy import UTCDateTime
from obspy.clients.fdsn import Client
import matplotlib.pyplot as plt
client = Client("IRIS")

# 2. Define parameters
start = UTCDateTime("2024-01-01T00:00:00")
duration = 3600

# 3. Download
st = client.get_waveforms("IU", "ANMO", "00", "BHZ", 
                          start, start+duration)

# 4. Process
st.detrend("linear")
st.filter("bandpass", freqmin=0.1, freqmax=10.0)

# 5. Plot
st.plot()

# 6. Analyze
trace = st[0]
print(f"Max amplitude: {np.max(np.abs(trace.data))}")

# 7. Save
st.write("processed.mseed", format="MSEED")
```

---

## 🎓 Remember

1. **Always make a copy** before processing:
   ```python
   st_filtered = st.copy()
   ```

2. **Check data before plotting**:
   ```python
   print(st)  # Shows if data loaded
   ```

3. **Use appropriate filters** for your frequency range

4. **Save your work** regularly

5. **Ask AI** when stuck!

---

**Print this and keep it visible while you code!** 📌

