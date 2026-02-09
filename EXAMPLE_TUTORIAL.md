# Example 1: 你的第一個地震學程式

這是一個簡單的逐步教學，幫助你開始進行地震資料分析。

## 你將學到什麼
- 從資料中心載入地震資料
- 視覺化地震波形
- 計算基本地震參數
- 使用 AI 協助你編程

## 先決條件
- 完成 [SETUP_GUIDE.md](../SETUP_GUIDE.md) 中的設定
- Google Colab 或本地 Python 環境
- 網際網路連線（用於下載資料）

---

## 步驟 1：匯入函式庫

首先，讓我們匯入需要的工具：

```python
# Import seismology library
from obspy import UTCDateTime
from obspy.clients.fdsn import Client
import matplotlib.pyplot as plt

# Import numerical tools
import numpy as np

print("✅ All libraries imported successfully!")
```

**💡 AI 提示：** 如果你遇到匯入錯誤，可以詢問 Gemini：「為什麼我會遇到 obspy 的 ImportError？」

---

## 步驟 2：連線到資料中心

我們將連線到 IRIS，一個主要的地震學資料庫：

```python
# Create a client to access IRIS data
client = Client("IRIS")
print("📡 Connected to IRIS data center!")
```

**🤔 什麼是 IRIS？**
IRIS (Incorporated Research Institutions for Seismology) 提供來自全球數千個測站的地震資料。

**💡 AI 提示：** 詢問 NotebookLM：「什麼是 IRIS 資料中心？」

---

## 步驟 3：下載真實地震資料

讓我們取得最近一次重大地震的資料：

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

**📝 理解參數：**
- `network`：營運測站的組織
- `station`：特定地震儀位置（ANTO = 土耳其安卡拉）
- `channel`：感測器類型（BHZ = 寬頻、高增益、垂直分量）
- `location`：用於同一測站的多個感測器
- `starttime/endtime`：資料的時間窗口

**💡 AI 提示：** 詢問 Gemini：「解釋像 BHZ 這樣的 SEED 通道代碼」

---

## 步驟 4：視覺化資料

現在讓我們看看地震的樣子：

```python
# Quick plot
stream.plot(size=(800, 400))
```

**🎯 你看到的內容：**
- **X 軸：** 時間（秒或分鐘）
- **Y 軸：** 地面運動（計數或速度）
- **尖峰：** 不同地震波的到達

**💡 AI 提示：** 詢問：「P 波和 S 波在地震圖上看起來是什麼樣子？」

---

## 步驟 5：取得詳細資訊

讓我們更仔細地檢查資料：

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

## 步驟 6：處理資料

讓我們透過去除雜訊來清理資料：

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

**🤔 為什麼要過濾？**
過濾器可以去除不需要的雜訊，並專注於地震訊號最強的頻率範圍。

**💡 AI 提示：** 詢問：「什麼是地震學中的帶通濾波器？」

---

## 步驟 7：比較原始資料與過濾後資料

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

## 步驟 8：計算基本參數

讓我們提取一些有用的資訊：

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

## 步驟 9：識別波的到達

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

**💡 AI 提示：** 詢問：「我如何自動偵測 P 波和 S 波的到達？」

---

## 步驟 10：儲存你的工作

```python
# Save the processed data
stream_filtered.write("processed_earthquake.mseed", format="MSEED")
print("💾 Saved processed data to 'processed_earthquake.mseed'")

# Save the plot
fig.savefig("earthquake_plot.png", dpi=300, bbox_inches='tight')
print("💾 Saved plot to 'earthquake_plot.png'")
```

---

## 🎉 恭喜！

你已經完成了你的第一個地震學程式！你學會了：
- ✅ 連線到地震資料中心
- ✅ 下載真實地震資料
- ✅ 視覺化地震圖
- ✅ 過濾和處理地震訊號
- ✅ 計算基本參數
- ✅ 識別波的到達

---

## 🚀 下一步

### 嘗試這些修改：

1. **不同測站：**
   將 `station="ANTO"` 改為其他測站，例如：
   - `station="ANMO"`（美國）
   - `station="TATO"`（台灣）
   - `station="COLA"`（阿拉斯加）

2. **不同地震：**
   更改 `starttime` 以分析其他地震：
   ```python
   # 2011 Tohoku Earthquake (Japan)
   starttime = UTCDateTime("2011-03-11T05:46:00")
   
   # 2023 Morocco Earthquake
   starttime = UTCDateTime("2023-09-08T22:11:00")
   ```

3. **三個分量：**
   下載所有三個分量（垂直、北向、東向）：
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

### 練習題：

**練習 1：尋找當地地震**
- 使用 USGS 地震目錄查找最近的事件
- 從附近測站下載資料
- 比較不同距離的波形

**練習 2：測量走時**
- 計算 P 波和 S 波之間的時間差
- 估計到地震的距離
- 與實際距離進行比較

**練習 3：頻率分析**
- 建立資料的頻譜圖
- 識別主要頻率
- 比較過濾前後的結果

---

## 🤖 使用 AI 進行學習

### 可以問的好問題：

**概念性問題：**
- 「為什麼 P 波比 S 波傳播得更快？」
- 「什麼導致地震中的表面波？」
- 「地震規模是如何計算的？」

**技術性問題：**
- 「我如何從多個測站下載資料？」
- 「區域地震的最佳濾波器是什麼？」
- 「我如何在不同的時間格式之間轉換？」

**除錯問題：**
- 「為什麼我的 stream 是空的？」
- 「我如何修復『無可用資料』錯誤？」
- 「這個 ObsPy 警告是什麼意思？」

---

## 📚 其他資源

### 推薦閱讀：
1. ObsPy Tutorial: https://docs.obspy.org/tutorial/
2. Seismology and the Earth's Interior
3. Introduction to Seismology by Shearer

### 可探索的資料集：
1. Recent earthquakes: https://earthquake.usgs.gov/
2. Continuous data: IRIS DMC
3. Event catalogs: ISC, USGS

### 社群：
- ObsPy Users Forum
- Seismology Stack Exchange
- GitHub ObsPy Issues

---

**祝編程愉快！記住：學習的最好方式是實作。嘗試、失敗、學習、重複！** 🌍📊🐍

