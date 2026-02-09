# 📋 快速參考手冊 - 地震學第一天

**編寫程式碼時請隨時參考！**

---

## 🚀 開始使用（Google Colab）

### 1. 設定（僅執行一次）
```python
!pip install obspy -q
```

### 2. 匯入函式庫
```python
from obspy import UTCDateTime
from obspy.clients.fdsn import Client
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline
```

### 3. 連接到資料源
```python
client = Client("IRIS")
```

---

## 📡 下載資料

### 基本下載
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

### 快速下載近期資料
```python
t = UTCDateTime() - 86400  # 24 hours ago
st = client.get_waveforms("IU", "ANMO", "00", "BHZ", t, t+3600)
```

### 多個分量
```python
# Use BH* to get BHZ, BHN, BHE
st = client.get_waveforms("IU", "ANMO", "00", "BH*", t, t+3600)
```

---

## 📊 檢視與繪製資料

### 快速檢視
```python
print(st)              # Show info
st.plot()              # Quick plot
```

### 自訂繪圖
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

## 🔧 處理資料

### 濾波
```python
# Bandpass filter (keep frequencies between 0.1 and 10 Hz)
st_filtered = st.copy()
st_filtered.filter("bandpass", freqmin=0.1, freqmax=10.0)
```

### 去趨勢
```python
st.detrend("linear")    # Remove linear trend
st.detrend("demean")    # Remove mean
```

### 重新採樣
```python
st.resample(20.0)       # Resample to 20 Hz
```

---

## 📈 分析

### 基本統計
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

### 尋找峰值
```python
peak_index = np.argmax(np.abs(data))
peak_time = trace.times()[peak_index]
peak_value = data[peak_index]
print(f"Peak at {peak_time:.2f}s: {peak_value}")
```

---

## 💾 儲存資料

### 儲存串流
```python
st.write("output.mseed", format="MSEED")
st.write("output.sac", format="SAC")
```

### 儲存繪圖
```python
plt.savefig("plot.png", dpi=300, bbox_inches='tight')
```

---

## 🎯 常用測站代碼

| 代碼 | 位置 | 類型 |
|------|----------|------|
| ANMO | New Mexico, USA | Broadband |
| ANTO | Ankara, Turkey | Broadband |
| COLA | Alaska, USA | Broadband |
| TATO | Taiwan | Broadband |
| MBWA | Zimbabwe | Broadband |

---

## 📍 通道代碼

### 格式：[頻段][儀器][分量]

**頻段：**
- `B` = Broadband（寬頻，0.1-10 Hz）
- `H` = High Broadband（高寬頻，10-80 Hz）
- `L` = Long Period（長週期，< 0.1 Hz）

**儀器：**
- `H` = High Gain Seismometer（高增益地震儀）
- `L` = Low Gain Seismometer（低增益地震儀）
- `N` = Accelerometer（加速度計）

**分量：**
- `Z` = Vertical（垂直）
- `N` = North-South（南北向）
- `E` = East-West（東西向）
- `1,2,3` = Orthogonal components（正交分量）

**範例：**
- `BHZ` = Broadband, High-gain, Vertical（寬頻、高增益、垂直）
- `HHN` = High-broadband, High-gain, North（高寬頻、高增益、北向）
- `LHE` = Long-period, High-gain, East（長週期、高增益、東向）

---

## ⏰ 時間格式

### 建立時間物件
```python
# From string
t = UTCDateTime("2024-01-01T12:00:00")

# Current time
t = UTCDateTime()

# Relative time
t = UTCDateTime() - 3600  # 1 hour ago
```

### 時間運算
```python
t1 = UTCDateTime("2024-01-01T00:00:00")
t2 = t1 + 3600            # Add 1 hour
diff = t2 - t1            # Difference in seconds
```

---

## 🐛 常見錯誤與修正

### 無可用資料
```python
# Problem: No data for time window
# Fix: Check earthquake time, adjust window
# Try: USGS earthquake catalog for exact times
```

### 匯入錯誤
```python
# Problem: No module named 'obspy'
# Fix: Run !pip install obspy
```

### 空白繪圖
```python
# Problem: Plot shows nothing
# Fix: Check data is not empty: print(st)
# Add: %matplotlib inline in Colab
```

### 下載速度慢
```python
# Problem: Download takes too long
# Fix: Reduce time window
# Or: Try different client: Client("USGS")
```

---

## 🤖 AI 協助指令

**在 Colab 中：**
- 點擊 🤖 圖示
- 或按 `Ctrl + Alt + Enter`

**良好的提問方式：**
```
"How do I [specific task]?"
"Why is [error message] happening?"
"Explain [concept] in simple terms"
"Debug this code: [paste code]"
```

---

## 🔗 快速連結

- **IRIS Data**: https://www.iris.edu/
- **USGS Earthquakes**: https://earthquake.usgs.gov/
- **ObsPy Docs**: https://docs.obspy.org/
- **Colab**: https://colab.research.google.com/
- **NotebookLM**: https://notebooklm.google.com/

---

## 📝 工作流程範本

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

## 🎓 注意事項

1. **處理前務必複製備份**：
   ```python
   st_filtered = st.copy()
   ```

2. **繪圖前檢查資料**：
   ```python
   print(st)  # Shows if data loaded
   ```

3. **使用適合您頻率範圍的濾波器**

4. **定期儲存您的工作**

5. **遇到困難時尋求 AI 協助！**

---

**請列印此手冊並在編程時保持可見！** 📌

