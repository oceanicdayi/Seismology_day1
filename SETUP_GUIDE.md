# 設定指南：開始使用地震學編程

歡迎來到地震學第一天課程！本指南將幫助您設定環境並開始使用 AI 輔助學習。

## 快速開始（推薦初學者）

### 選項 1: Google Colab（無需安裝） ⚡

這是**最簡單且推薦**的入門方式！

#### 步驟 1：訪問 Google Colab
1. 打開您的網頁瀏覽器
2. 前往：https://colab.research.google.com/
3. 使用您的 Google 帳戶登入
4. 點擊「New Notebook」

#### 步驟 2：測試您的環境
將此代碼複製並貼到儲存格中，然後按 `Shift + Enter`：

```python
import sys
print(f"Python version: {sys.version}")
print("✅ Your environment is ready!")
```

#### 步驟 3：安裝地震學函式庫
在新儲存格中執行此代碼：

```python
# Install seismology tools
!pip install obspy numpy matplotlib pandas

# Test installation
import obspy
print(f"✅ ObsPy version: {obspy.__version__}")
print("🎉 All libraries installed successfully!")
```

#### 步驟 4：啟用 Gemini AI 助理
1. 點擊左側邊欄的「🤖」圖示
2. 或使用 `Ctrl + Alt + Enter` 打開 AI 聊天
3. 嘗試詢問：「How do I load seismic data in Python?」

**就是這樣！您已準備好開始編程！** 🚀

---

## AI 學習工具設定

### 設定 NotebookLM

NotebookLM 是您的 AI 驅動學習夥伴，可以從教科書中提取知識。

#### 步驟 1：訪問 NotebookLM
1. 前往：https://notebooklm.google.com/
2. 使用您的 Google 帳戶登入
3. 點擊「New Notebook」

#### 步驟 2：上傳課程資料
1. 點擊「Add Source」
2. 上傳選項：
   - 地震學教科書的 PDF
   - Google Drive 文件
   - 網頁（課程大綱、閱讀材料）
   - YouTube 視頻（講座）

#### 步驟 3：開始學習
嘗試以下範例查詢：

**基本概念：**
```
"What are P-waves and S-waves?"
"Explain the difference between magnitude and intensity"
"How do seismometers work?"
```

**編程幫助：**
```
"How do I process seismic data in Python?"
"What is the ObsPy library used for?"
"Show me examples of plotting seismic waveforms"
```

**學習指南：**
```
"Create a summary of Chapter 3"
"What are the key concepts about earthquake location?"
"Make a study guide for seismic wave propagation"
```

### 有效使用 Gemini AI

#### 在 Google Colab 中
Gemini 直接整合到 Colab 中：

1. **代碼生成：**
   ```
   提示詞：「Write Python code to plot a sine wave」
   Gemini 會為您生成代碼！
   ```

2. **錯誤調試：**
   ```
   當您遇到錯誤時，詢問：
   「Why am I getting a NameError in this code?」
   ```

3. **解釋：**
   ```
   選擇代碼並詢問：
   「Explain what this code does」
   ```

#### 有效提示詞技巧

**好的提示詞：**
- ✅ "Write Python code to load a seismic file in miniSEED format using ObsPy"
- ✅ "Explain the Richter magnitude scale in simple terms"
- ✅ "Debug this error: ImportError: No module named 'obspy'"

**效果較差的提示詞：**
- ❌ "Code for seismology"（太模糊）
- ❌ "Help"（沒有上下文）
- ❌ "Fix it"（AI 不知道「它」是什麼）

---

## 選項 2：本地安裝（進階使用者）

如果您偏好在本地機器上工作：

### 先決條件
- Python 3.8 或更高版本
- Git（可選）
- 文字編輯器或 IDE（推薦 VS Code）

### 安裝步驟

#### Windows

1. **安裝 Python：**
   - 從此處下載：https://www.python.org/downloads/
   - 安裝時勾選「Add Python to PATH」
   - 驗證：打開命令提示字元並輸入 `python --version`

2. **安裝函式庫：**
   ```cmd
   pip install obspy numpy matplotlib pandas jupyter
   ```

3. **啟動 Jupyter：**
   ```cmd
   jupyter notebook
   ```

#### macOS

1. **安裝 Python（使用 Homebrew）：**
   ```bash
   brew install python
   ```

2. **安裝函式庫：**
   ```bash
   pip3 install obspy numpy matplotlib pandas jupyter
   ```

3. **啟動 Jupyter：**
   ```bash
   jupyter notebook
   ```

#### Linux (Ubuntu/Debian)

1. **安裝 Python：**
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```

2. **安裝函式庫：**
   ```bash
   pip3 install obspy numpy matplotlib pandas jupyter
   ```

3. **啟動 Jupyter：**
   ```bash
   jupyter notebook
   ```

---

## 驗證測試

執行以下測試以確保一切正常運作：

### 測試 1：基本 Python
```python
# Test basic Python
x = [1, 2, 3, 4, 5]
print(f"Sum: {sum(x)}")
print("✅ Python works!")
```

### 測試 2：NumPy
```python
# Test NumPy
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(f"Mean: {np.mean(arr)}")
print("✅ NumPy works!")
```

### 測試 3：Matplotlib
```python
# Test Matplotlib
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title("Test Plot")
plt.show()
print("✅ Matplotlib works!")
```

### 測試 4：ObsPy
```python
# Test ObsPy
from obspy import read
from obspy.clients.fdsn import Client

client = Client("IRIS")
print("✅ ObsPy works!")
print("🎉 You can download real seismic data!")
```

---

## 獲取您的第一個地震資料

讓我們下載真實的地震資料！

```python
from obspy import UTCDateTime
from obspy.clients.fdsn import Client

# Connect to IRIS data center
client = Client("IRIS")

# Define time window (example: recent earthquake)
starttime = UTCDateTime("2024-01-01T00:00:00")
endtime = starttime + 3600  # 1 hour of data

# Download data
print("📡 Downloading seismic data...")
st = client.get_waveforms(
    network="IU",      # Network code
    station="ANMO",    # Station code
    location="00",     # Location code
    channel="BHZ",     # Channel code (vertical)
    starttime=starttime,
    endtime=endtime
)

print(f"✅ Downloaded {len(st)} trace(s)")
print(st)

# Plot the data
st.plot()
```

---

## 疑難排解

### 常見問題

**問題：「pip command not found」**
- **解決方案：** Python 不在 PATH 中。重新安裝 Python 並勾選「Add to PATH」

**問題：「No module named 'obspy'」**
- **解決方案：** 執行 `pip install obspy` 或 `pip3 install obspy`

**問題：Linux/Mac 上出現「Permission denied」**
- **解決方案：** 使用 `pip3 install --user obspy`

**問題：在 Jupyter 中看不到圖表**
- **解決方案：** 在筆記本開頭加入 `%matplotlib inline`

**問題：Colab 斷線**
- **解決方案：** 點擊「Reconnect」或重新整理頁面

**問題：下載速度緩慢**
- **解決方案：** 嘗試不同的 FDSN 客戶端（例如使用「USGS」代替「IRIS」）

### 獲取幫助

1. **詢問 Gemini AI：** 在 Colab 聊天中描述您的問題
2. **查看文件：** https://docs.obspy.org/
3. **使用 NotebookLM：** 上傳錯誤訊息並尋求解釋
4. **詢問講師：** 在辦公時間或論壇中
5. **社群：** ObsPy 論壇、Stack Overflow

---

## 下一步

設定好環境後：

1. ✅ 完成上述驗證測試
2. ✅ 下載您的第一個地震資料
3. ✅ 使用課程資料設定 NotebookLM
4. ✅ 練習使用 Gemini 獲取編程幫助
5. ✅ 查看 [PROPOSAL.md](PROPOSAL.md) 以了解課程概述
6. ✅ 打開第一個教學筆記本

---

## 快速參考卡

### 基本命令

```python
# Import libraries
import obspy
import numpy as np
import matplotlib.pyplot as plt

# Download data
from obspy.clients.fdsn import Client
client = Client("IRIS")

# Read local file
from obspy import read
st = read("path/to/file.mseed")

# Plot
st.plot()

# Get info
print(st)

# Filter data
st.filter("bandpass", freqmin=1.0, freqmax=10.0)
```

### 實用的 AI 提示詞

- "Load seismic data from IRIS"
- "Plot a seismogram with time on x-axis"
- "Calculate earthquake magnitude"
- "Filter seismic noise from data"
- "Explain this error message: [paste error]"

---

## 資源

### 官方文件
- **ObsPy:** https://docs.obspy.org/
- **NumPy:** https://numpy.org/doc/
- **Matplotlib:** https://matplotlib.org/stable/
- **Python:** https://docs.python.org/3/

### 資料來源
- **IRIS:** https://www.iris.edu/
- **USGS:** https://earthquake.usgs.gov/
- **ORFEUS:** https://www.orfeus-eu.org/

### 學習資源
- **ObsPy Tutorial:** https://docs.obspy.org/tutorial/
- **Python for Seismology:** https://krischer.github.io/seismo_live/
- **Seismology Datasets:** https://ds.iris.edu/ds/nodes/dmc/

---

**準備好開始您的地震學之旅了嗎？讓我們開始編程吧！** 🌍📊🐍

