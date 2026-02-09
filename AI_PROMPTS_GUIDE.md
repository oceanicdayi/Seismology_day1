# 地震學學習的 AI 提示詞指南

本指南提供有效的提示詞，協助使用 Gemini AI 和 NotebookLM 學習地震學與編程。

## 🤖 在 Google Colab 中使用 Gemini AI

### 開始使用程式碼生成

#### 基本提示詞
```
"Write Python code to import ObsPy and NumPy"
"Create a simple plot of a sine wave using matplotlib"
"Show me how to read a miniSEED file"
```

#### 地震學專用提示詞
```
"Write code to download seismic data from IRIS for station ANMO"
"Generate Python code to plot a seismogram with time on x-axis"
"Create code to apply a bandpass filter to seismic data"
"Show me how to calculate the envelope of a seismic trace"
```

### 除錯協助

#### 錯誤理解
```
"Explain this error: ImportError: No module named 'obspy'"
"Why am I getting 'No data available for request' from FDSN?"
"What does this warning mean: [warning message]"
"Debug this code: [paste your code]"
```

#### 程式碼改進
```
"How can I make this plot look better?"
"Is there a more efficient way to write this loop?"
"Why is my code running slowly?"
"How do I add error handling to this function?"
```

### 學習與解釋

#### 概念解釋
```
"Explain what P-waves and S-waves are in simple terms"
"What is the difference between magnitude and intensity?"
"How does a seismometer work?"
"Explain the concept of transfer function in seismology"
```

#### 程式碼解釋
```
"Explain what this ObsPy function does: stream.filter()"
"What are the parameters for UTCDateTime?"
"Break down this code line by line: [paste code]"
"What is the purpose of stream.detrend()?"
```

### 進階任務

#### 資料處理
```
"How do I remove instrument response from seismic data?"
"Write code to pick P-wave arrivals automatically"
"Show me how to rotate components to radial/transverse"
"Create a spectrogram of seismic data"
```

#### 分析
```
"Calculate earthquake magnitude from amplitude"
"How do I compute particle motion from three-component data?"
"Write code to calculate signal-to-noise ratio"
"Generate code for frequency-wavenumber analysis"
```

---

## 📚 使用 NotebookLM 學習地震學

### 初始設定

**上傳資料：**
1. Seismology textbook PDFs
2. Course lecture notes
3. ObsPy documentation
4. Research papers

### 有效的查詢模式

#### 理解概念

**基本問題：**
```
"What are body waves versus surface waves?"
"Explain the difference between Love and Rayleigh waves"
"How do earthquakes generate seismic waves?"
"What is seismic anisotropy?"
```

**深入探討：**
```
"Create a detailed explanation of earthquake location methods"
"Compare different magnitude scales (ML, Mw, Mb)"
"Explain tomographic imaging in seismology"
"What are the main challenges in earthquake prediction?"
```

#### 學習指南與摘要

**章節摘要：**
```
"Summarize Chapter 3 on seismic wave propagation"
"Create bullet points of key concepts from the elasticity chapter"
"What are the main takeaways from the section on ray theory?"
```

**概念圖：**
```
"Create a concept map connecting earthquake source, wave propagation, and recording"
"List all the relationships between magnitude, moment, and energy"
"Outline the steps from earthquake occurrence to seismogram"
```

#### 問題解決

**作業協助：**
```
"How do I approach calculating travel times?"
"What formula should I use for epicentral distance?"
"Walk me through the process of picking phase arrivals"
```

**練習題：**
```
"Generate practice problems on wave velocity calculations"
"Create example questions about magnitude calculations"
"Give me scenarios to practice earthquake location"
```

---

## 💡 有效提示的技巧

### 具體明確

**❌ 模糊：**
```
"Help with seismology"
"Code not working"
"Explain earthquakes"
```

**✅ 具體：**
```
"Explain how to download seismic data from the USGS using ObsPy"
"Why is my bandpass filter code giving an error about frequency limits?"
"What is the physical mechanism of P-wave generation in earthquakes?"
```

### 提供背景資訊

**❌ 無背景資訊：**
```
"Fix this"
"What's wrong?"
```

**✅ 有背景資訊：**
```
"I'm trying to plot seismic data but getting an empty plot. Here's my code: [code]"
"I'm learning about magnitude scales and confused about the difference between ML and Mw"
```

### 分解複雜任務

**❌ 過於複雜：**
```
"Build a complete earthquake analysis program"
```

**✅ 步驟分解：**
```
1. "How do I download data from multiple stations?"
2. "How do I synchronize the time windows?"
3. "How do I plot all traces together?"
4. "How do I measure arrival times on each trace?"
```

### 提出後續問題

**漸進式學習：**
```
1. "What is a seismogram?"
2. "How do I read a seismogram in Python?"
3. "How do I filter the seismogram?"
4. "How do I identify different wave phases?"
5. "How do I measure wave amplitudes?"
```

---

## 🎯 領域專用提示詞模板

### 資料獲取

```
"How do I download [time period] of data from [station] on the [network] network?"
"What are the available stations near [location]?"
"How do I search for earthquakes in [region] with magnitude > [value]?"
```

### 資料處理

```
"Apply a [filter type] filter with [parameters] to [data type]"
"Remove [artifact type] from [data]"
"Convert [input format] to [output format]"
```

### 視覺化

```
"Create a [plot type] showing [data] with [specific features]"
"Plot [multi-component data] in [layout] format"
"Generate a [map type] with [stations/earthquakes]"
```

### 分析

```
"Calculate [parameter] from [data] using [method]"
"Detect [feature] in [signal] with [algorithm]"
"Compare [data1] and [data2] using [metric]"
```

---

## 🚀 進階提示技巧

### 思考鏈

**要求 AI 逐步思考：**
```
"Walk me through the logic of calculating earthquake magnitude step by step"
"Explain your reasoning for why this code isn't working"
"Break down the physics behind P-wave velocity variations"
```

### 提供範例

**展示你想要的內容：**
```
"Generate code similar to this example but for downloading S-waves: [example code]"
"Create a plot like this but with different colors: [description]"
```

### 要求替代方案

**獲取多個選項：**
```
"Show me three different ways to filter seismic data"
"What are alternative methods for picking phase arrivals?"
"Compare different approaches to plotting seismograms"
```

### 要求解釋

**理解原因：**
```
"Why do we use this formula for magnitude?"
"Why is this method better than that one?"
"What are the limitations of this approach?"
```

---

## 📊 學習會話範例

### 會話 1：載入資料

1. **從基礎開始：**
   ```
   "How do I connect to the IRIS data center in Python?"
   ```

2. **建立在其上：**
   ```
   "How do I specify a time window for data download?"
   ```

3. **增加複雜度：**
   ```
   "How do I download data from multiple stations at once?"
   ```

4. **疑難排解：**
   ```
   "I'm getting 'No data available' - what could be wrong?"
   ```

5. **優化：**
   ```
   "How can I make this code more efficient?"
   ```

### 會話 2：理解概念

1. **基本理解：**
   ```
   NotebookLM: "What are seismic phases?"
   ```

2. **深入探討：**
   ```
   NotebookLM: "Explain the travel time curves for different phases"
   ```

3. **應用：**
   ```
   Gemini: "Write code to calculate theoretical arrival times"
   ```

4. **驗證：**
   ```
   NotebookLM: "How do theoretical times compare to observed times?"
   ```

---

## 🎓 主題專用提示詞

### 波傳播

```
"Explain Snell's law in the context of seismic waves"
"How do velocity discontinuities affect wave paths?"
"What causes seismic wave dispersion?"
"Code to simulate wave propagation through layers"
```

### 地震震源

```
"What is the focal mechanism of an earthquake?"
"Explain the double-couple source model"
"How is seismic moment related to magnitude?"
"Calculate moment from slip, area, and rigidity"
```

### 信號處理

```
"What is the purpose of detrending seismic data?"
"Explain the difference between causal and acausal filters"
"How do I choose appropriate filter parameters?"
"Implement a Butterworth filter in Python"
```

### 儀器設備

```
"How does a seismometer differ from an accelerometer?"
"What is instrument response and why remove it?"
"Explain the units in seismic data (counts, velocity, acceleration)"
"Convert between different ground motion units"
```

---

## 🔄 迭代提示模式

### 學習循環

1. **提問**：請求資訊或程式碼
2. **審查**：閱讀並嘗試理解回應
3. **測試**：執行程式碼或應用概念
4. **精煉**：提出後續問題
5. **擴展**：建立在你學到的知識上

### 範例循環

```
Round 1: "How do I plot a seismogram?"
[Get code, try it]

Round 2: "The plot is too small, how do I make it bigger?"
[Adjust code]

Round 3: "How do I add axis labels and a title?"
[Enhance plot]

Round 4: "Can I plot multiple seismograms together?"
[Expand capability]

Round 5: "How do I save this plot as a high-resolution image?"
[Polish output]
```

---

## ⚡ 快速參考提示詞

### 常見任務

**資料下載：**
```
"Download data: network=[NET], station=[STA], start=[TIME], duration=[MINS]"
```

**基本繪圖：**
```
"Plot seismic trace with time in minutes on x-axis"
```

**濾波：**
```
"Apply bandpass filter [FMIN]-[FMAX] Hz"
```

**儲存：**
```
"Save processed data as [FORMAT]"
```

### 疑難排解

**匯入錯誤：**
```
"How do I install [library]?"
```

**空輸出：**
```
"Data request returns empty - debug: [query details]"
```

**繪圖問題：**
```
"Plot showing [problem] - code: [code snippet]"
```

**效能：**
```
"Code slow for [data size] - optimize: [code]"
```

---

## 🌟 最佳實踐

### 應該做的 ✅

- 從簡單開始，逐步增加複雜度
- 相關時提供程式碼範例
- 指定確切的錯誤訊息
- 要求解釋回應內容
- 迭代並精煉提示詞
- 儲存有用的提示詞以便重複使用

### 不應該做的 ❌

- 不要貼上整個錯誤追蹤記錄（總結關鍵資訊）
- 不要一次問多個不相關的問題
- 不要假設 AI 知道你的資料結構
- 不要跳過測試建議的程式碼
- 不要忘記問「為什麼」事情會這樣運作

---

## 🎯 目標導向的提示詞框架

### 理解用

```
"I want to understand [CONCEPT]
- Start with a simple explanation
- Give an analogy
- Explain the physics/math
- Show a practical example
- List common misconceptions"
```

### 編程用

```
"I need to [TASK]
- My data format is [FORMAT]
- I want output as [OUTPUT]
- Constraints: [CONSTRAINTS]
- Show the code and explain key parts"
```

### 除錯用

```
"My code isn't working:
- Goal: [WHAT I'M TRYING TO DO]
- Current behavior: [WHAT HAPPENS]
- Expected: [WHAT SHOULD HAPPEN]
- Code: [RELEVANT CODE]
- Error: [ERROR MESSAGE]"
```

---

**掌握這些提示技巧，你將學得更快、編程更好、理解更深！** 🚀

