# 🌍 地震學第一天：AI 增強學習環境

歡迎來到**地震學第一天課程**！本儲存庫提供了使用現代 AI 工具和編程實踐開始學習地震學所需的一切。

## 🎯 內容包括

本課程使用 **Google Colab**（我們的「反重力」平台）透過 AI 輔助教授地震學編程：

- **無需安裝** - 在瀏覽器中立即開始編程
- **AI 驅動學習** - 使用 Gemini 和 NotebookLM 獲得個人化幫助
- **真實地震數據** - 使用實際地震記錄
- **逐步教學** - 易於遵循的說明和範例
- **互動式筆記本** - 透過實作學習，而非僅閱讀

## 📚 文檔

### 必讀資料
1. **[PROPOSAL.md](PROPOSAL.md)** - 完整課程提案與方法論
2. **[SETUP_GUIDE.md](SETUP_GUIDE.md)** - 逐步環境設置說明
3. **[EXAMPLE_TUTORIAL.md](EXAMPLE_TUTORIAL.md)** - 詳細演練與說明

### 快速開始
- **[first_day_tutorial.ipynb](first_day_tutorial.ipynb)** - 互動式 Jupyter 筆記本，立即開始

## 🚀 快速入門指南

### 適合完全初學者（推薦）

1. **開啟 Google Colab**（無需安裝！）
   - 前往：https://colab.research.google.com/
   - 使用您的 Google 帳號登入
   - 上傳 `first_day_tutorial.ipynb` 或建立新筆記本

2. **安裝地震學工具**（一行指令！）
   ```python
   !pip install obspy numpy matplotlib pandas
   ```

3. **下載您的第一筆地震數據**
   ```python
   from obspy.clients.fdsn import Client
   from obspy import UTCDateTime
   
   client = Client("IRIS")
   st = client.get_waveforms("IU", "ANMO", "00", "BHZ",
                             UTCDateTime("2024-01-01"), 
                             UTCDateTime("2024-01-01") + 3600)
   st.plot()
   ```

4. **就是這樣！** 🎉 您正在分析真實的地震數據！

### 適合有經驗的使用者

如果您偏好本地安裝：
```bash
pip install -r requirements.txt
jupyter notebook first_day_tutorial.ipynb
```

## 🤖 AI 學習工具

### Gemini AI（內建於 Colab）
- **程式碼生成**：請 Gemini 為您編寫程式碼
- **除錯**：獲得修復錯誤的幫助
- **解釋**：理解程式碼的作用
- **文檔**：快速查找函數

**使用方法：**
- 在 Colab 中，點擊 🤖 圖示或按 `Ctrl + Alt + Enter`
- 詢問問題，例如：「如何過濾地震數據？」

### NotebookLM
- **知識提取**：上傳教科書並獲得 AI 摘要
- **問答**：詢問有關地震學概念的問題
- **學習指南**：生成個人化學習材料

**設置：**
1. 前往：https://notebooklm.google.com/
2. 上傳您的地震學教科書（PDF）
3. 提問並學習！

## 📖 課程理念

### 「反重力」方法

傳統地震學課程可能令人生畏：
- ❌ 複雜的軟體安裝
- ❌ 困難的數學概念
- ❌ 有限的數據存取
- ❌ 緩慢的反饋迴圈

我們的方法消除了這些障礙：
- ✅ **零安裝**：在瀏覽器中編程，使用 Google Colab
- ✅ **AI 輔助**：從 Gemini 獲得全天候幫助
- ✅ **真實數據**：存取數千個地震站
- ✅ **立即結果**：幾秒鐘內看到地震
- ✅ **從實作中學習**：互動式、實作導向的方法

### 學習目標

在第一天結束時，您將能夠：
1. ✅ 設置地震學編程環境
2. ✅ 使用 AI 工具進行學習和編程
3. ✅ 下載真實地震數據
4. ✅ 視覺化地震波形
5. ✅ 處理和過濾地震信號
6. ✅ 計算基本地震學參數
7. ✅ 使用 Python 進行數據分析

## 🎓 您將學到什麼

### 技術技能
- Python 編程基礎
- 使用 ObsPy 進行地震數據處理
- 使用 Matplotlib 進行數據視覺化
- 時間序列數據處理
- 信號處理基礎

### 地震學概念
- 地震波（P 波、S 波、表面波）
- 地震儀數據解讀
- 數據過濾與降噪
- 波形到達識別
- 基本地震定位原理

### AI 與學習技能
- 有效的 AI 提示技巧
- 使用 AI 生成程式碼
- AI 輔助除錯
- 從教科書中提取知識
- 自主學習策略

## 📂 儲存庫結構

```
Seismology_day1/
├── README.md                    # 本文件
├── PROPOSAL.md                  # 詳細課程提案
├── SETUP_GUIDE.md              # 環境設置說明
├── EXAMPLE_TUTORIAL.md         # 詳細演練
├── first_day_tutorial.ipynb    # 互動式筆記本
└── requirements.txt            # Python 依賴項
```

## 🛠️ 技術堆疊

- **Python 3.8+**：程式語言
- **ObsPy**：地震學數據處理
- **NumPy**：數值計算
- **Matplotlib**：數據視覺化
- **Pandas**：數據處理
- **Google Colab**：雲端開發
- **Gemini AI**：編程助手
- **NotebookLM**：學習夥伴

## 💡 教學理念

### 以學生為中心的學習
- 從簡單開始，逐步增加複雜度
- 透過實作學習，而非僅觀看
- 錯誤是學習的機會
- AI 作為學習夥伴，而非替代品

### 現代工具
- 使用專業人士使用的相同工具
- 利用 AI 增強學習
- 雲端化以提高可訪問性
- 開源以保持透明度

### 真實世界應用
- 使用實際地震數據
- 解決實際問題
- 建立可轉移的技能
- 為研究或產業做準備

## 🎯 成功指標

學生報告感到：
- **自信**在使用 Python 進行地震學研究
- **舒適**尋求 AI 幫助
- **有能力**獨立學習
- **興奮**繼續學習

目標成果：
- 100% 成功設置環境
- 90%+ 完成第一次分析
- 85%+ 感到有信心繼續
- 高度參與和滿意度

## 🤝 獲得幫助

### 課堂期間
- 詢問您的教師
- 在 Colab 中使用 Gemini AI
- 與同學合作
- 查看文檔

### 課後
- 複習教學材料
- 向 NotebookLM 提問
- 訪問 ObsPy 文檔
- 在討論論壇發文

### 常見問題
請參閱 [SETUP_GUIDE.md](SETUP_GUIDE.md#troubleshooting) 以獲取故障排除提示。

## 📖 其他資源

### 地震學
- **IRIS 教育**：https://www.iris.edu/hq/inclass
- **USGS 地震災害**：https://earthquake.usgs.gov/
- **ObsPy 教學**：https://docs.obspy.org/tutorial/

### Python 編程
- **Python.org**：https://www.python.org/
- **Real Python**：https://realpython.com/
- **Python 數據科學**：各種線上課程

### AI 工具
- **Google Colab**：https://colab.research.google.com/
- **Gemini AI**：內建於 Colab
- **NotebookLM**：https://notebooklm.google.com/

## 🌟 為什麼選擇這種方法？

### 傳統挑戰
學生經常在以下方面遇到困難：
- 複雜的軟體安裝
- 數學先決條件
- 有限的數據存取
- 緩慢的學習反饋

### 我們的解決方案
我們提供：
- **即時訪問**：在瀏覽器中編程，無需安裝
- **AI 輔導**：Gemini 和 NotebookLM 全天候幫助
- **真實數據**：數千次地震可供探索
- **引導式學習**：逐步教學
- **實用技能**：可就業的 Python 編程

### 結果
使用這種方法的學生：
- 更快開始編程（分鐘而非小時）
- 更有效地學習（AI 輔助）
- 感到更有信心（立即成功）
- 繼續學習（參與且有動力）

## 🎓 下一步

完成第一天後：
1. 練習不同的地震
2. 探索其他地震站
3. 嘗試挑戰練習
4. 閱讀其他材料
5. 為第二天的主題做準備

## 📄 授權

本教育材料供學習目的使用。請查看各個函式庫的授權條款以了解其使用條款。

## 🙏 致謝

- **IRIS** 提供地震數據訪問
- **ObsPy** 開發團隊
- **Google** 提供 Colab、Gemini 和 NotebookLM
- **地震學社群**提供開放數據和工具

## 📧 聯絡方式

關於本課程的問題或反饋：
- 在此儲存庫中開啟問題
- 聯繫您的課程教師
- 加入我們的討論論壇

---

**準備好開始您的地震學之旅了嗎？打開 [first_day_tutorial.ipynb](first_day_tutorial.ipynb) 開始編程吧！** 🌍📊🐍