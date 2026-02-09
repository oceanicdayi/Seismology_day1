# 🚀 快速入門 - 選擇您的路徑

**地震學和編程的新手？**您來對地方了！選擇最適合您的路徑：

---

## 🎯 快速路徑

### 路徑 1：「我想現在就開始編程！」（5 分鐘）

1. **開啟 Google Colab**：https://colab.research.google.com/
2. **建立新的 notebook**（或上傳 `first_day_tutorial.ipynb`）
3. **執行此程式碼**：
   ```python
   !pip install obspy -q
   from obspy import UTCDateTime
   from obspy.clients.fdsn import Client
   
   client = Client("IRIS")
   st = client.get_waveforms("IU", "ANMO", "00", "BHZ",
                             UTCDateTime("2024-01-01"),
                             UTCDateTime("2024-01-01")+3600)
   st.plot()
   ```
4. **您成功了！** 🎉 這是真實的地震資料！

**下一步**：開啟 [first_day_tutorial.ipynb](first_day_tutorial.ipynb) 進行完整教學

---

### 路徑 2：「我想先理解」（15 分鐘）

1. **閱讀**：[PROPOSAL.md](PROPOSAL.md) - 理解課程理念
2. **設定**：[SETUP_GUIDE.md](SETUP_GUIDE.md) - 逐步環境設定
3. **學習**：[EXAMPLE_TUTORIAL.md](EXAMPLE_TUTORIAL.md) - 詳細演練
4. **實作**：[first_day_tutorial.ipynb](first_day_tutorial.ipynb) - 實際編程

---

### 路徑 3：「我是教師」（20 分鐘）

1. **課程設計**：[PROPOSAL.md](PROPOSAL.md) - 完整方法論
2. **教學計畫**：[INSTRUCTOR_GUIDE.md](INSTRUCTOR_GUIDE.md) - 詳細教案
3. **學生資源**：所有其他文件
4. **準備**：檢閱 [first_day_tutorial.ipynb](first_day_tutorial.ipynb)

---

## 📚 完整文件概覽

| 文件 | 目的 | 時間 | 受眾 |
|----------|---------|------|----------|
| **[README.md](README.md)** | 儲存庫概覽 | 5 分鐘 | 所有人 |
| **[PROPOSAL.md](PROPOSAL.md)** | 課程提案與理念 | 15 分鐘 | 教師、規劃者 |
| **[SETUP_GUIDE.md](SETUP_GUIDE.md)** | 環境設定 | 10 分鐘 | 學生 |
| **[EXAMPLE_TUTORIAL.md](EXAMPLE_TUTORIAL.md)** | 詳細演練 | 30 分鐘 | 學生 |
| **[first_day_tutorial.ipynb](first_day_tutorial.ipynb)** | 互動式 notebook | 2 小時 | 學生 |
| **[AI_PROMPTS_GUIDE.md](AI_PROMPTS_GUIDE.md)** | 有效使用 AI | 20 分鐘 | 學生 |
| **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** | 速查表 | 5 分鐘 | 學生（隨時查閱） |
| **[INSTRUCTOR_GUIDE.md](INSTRUCTOR_GUIDE.md)** | 教學計畫 | 20 分鐘 | 教師 |
| **[requirements.txt](requirements.txt)** | Python 相依套件 | N/A | 技術設定 |

---

## 🎓 給學生

### 如果這是您第一次編程

**不要恐慌！**本課程專為完全初學者設計。

1. 從上面的**路徑 1** 開始（只需 5 分鐘！）
2. 閱讀 [SETUP_GUIDE.md](SETUP_GUIDE.md)
3. 完成 [first_day_tutorial.ipynb](first_day_tutorial.ipynb)
4. 遇到困難時使用 [QUICK_REFERENCE.md](QUICK_REFERENCE.md)
5. 閱讀 [AI_PROMPTS_GUIDE.md](AI_PROMPTS_GUIDE.md) 以獲得 AI 協助

**請記住：**
- 每個人都有起點
- 錯誤是我們學習的方式
- AI 會協助您（Gemini 與 NotebookLM）
- 勇於提問！

### 如果您已略懂 Python

**太好了！**您會學得更快。

1. 瀏覽 [PROPOSAL.md](PROPOSAL.md) 以理解教學方法
2. 直接跳到 [first_day_tutorial.ipynb](first_day_tutorial.ipynb)
3. 嘗試挑戰練習
4. 探索 [EXAMPLE_TUTORIAL.md](EXAMPLE_TUTORIAL.md) 的進階主題
5. 使用 [AI_PROMPTS_GUIDE.md](AI_PROMPTS_GUIDE.md) 進行 AI 輔助學習

### 如果您是地震學專家但程式設計新手

**歡迎！**將您的領域知識作為優勢。

1. 閱讀 [SETUP_GUIDE.md](SETUP_GUIDE.md) 進行 Python 設定
2. 完成 [first_day_tutorial.ipynb](first_day_tutorial.ipynb)
3. 使用 [AI_PROMPTS_GUIDE.md](AI_PROMPTS_GUIDE.md) - 向 Gemini 詢問程式碼問題
4. 使用 NotebookLM 搭配您的教科書
5. 隨時查閱 [QUICK_REFERENCE.md](QUICK_REFERENCE.md)

---

## 👨‍🏫 給教師

### 教授本課程

1. **閱讀** [PROPOSAL.md](PROPOSAL.md) - 理解教學理念
2. **檢閱** [INSTRUCTOR_GUIDE.md](INSTRUCTOR_GUIDE.md) - 詳細教案
3. **測試** [first_day_tutorial.ipynb](first_day_tutorial.ipynb) - 確保一切正常運作
4. **準備**：
   - 設定課堂 Google Colab
   - 測試 IRIS 資料存取
   - 使用課程資料建立 NotebookLM
   - 設定溝通管道

### 客製化教材

所有教材都是 markdown 格式，可以編輯：
- 調整範例以符合您的地區
- 新增當地地震案例
- 修改進度以配合您的學生
- 加入您的研究範例

### 獲得協助

- 在此儲存庫中開啟問題
- 聯絡原作者
- 加入教師社群（如有）

---

## 🤖 AI 學習工具

### 設定 AI 輔助

**Gemini AI（在 Google Colab 中）**
- 已整合，只需點擊 🤖 圖示
- 無需額外設定
- 免費使用

**NotebookLM**
1. 前往 https://notebooklm.google.com/
2. 建立新的 notebook
3. 上傳課程資料（PDF、文件）
4. 開始提問！

**參見** [AI_PROMPTS_GUIDE.md](AI_PROMPTS_GUIDE.md) 以了解有效的提示詞

---

## 🛠️ 技術設定

### 選項 1：Google Colab（推薦）
- ✅ 零安裝
- ✅ 適用於任何裝置
- ✅ 免費 GPU 存取
- ✅ 內建 AI

**只需前往**：https://colab.research.google.com/

### 選項 2：本機安裝

```bash
# Install Python dependencies
pip install -r requirements.txt

# Start Jupyter
jupyter notebook first_day_tutorial.ipynb
```

**參見** [SETUP_GUIDE.md](SETUP_GUIDE.md) 以了解詳細說明

---

## 🎯 學習目標

完成本課程後，您將能夠：

### 技術技能
- ✅ 使用 Google Colab 進行 Python 編程
- ✅ 安裝和匯入 Python 函式庫
- ✅ 下載真實的地震資料
- ✅ 建立資料視覺化
- ✅ 處理和過濾訊號
- ✅ 計算基本統計數據
- ✅ 除錯常見錯誤

### 地震學知識
- ✅ 理解地震波類型（P 波、S 波、表面波）
- ✅ 解讀地震圖
- ✅ 識別波的到達
- ✅ 理解資料格式和通道
- ✅ 了解資料來源（IRIS、USGS）

### AI 與學習技能
- ✅ 使用 AI 產生程式碼
- ✅ 使用 AI 輔助除錯
- ✅ 從教科書中擷取知識
- ✅ 獨立學習
- ✅ 有效的提示技巧

---

## 📊 時間估計

### 最短入門時間
- **5 分鐘**：執行第一個地震分析（路徑 1）

### 舒適的基礎
- **1-2 小時**：完成設定 + 教學 notebook

### 深入理解
- **3-4 小時**：閱讀所有資料 + 練習習題

### 教學準備
- **2-3 小時**：檢閱所有資料 + 測試程式碼

---

## ✅ 快速檢查清單

### 開始之前
- [ ] 我有網路連線
- [ ] 我有 Google 帳號（用於 Colab）
- [ ] 我已選擇我的學習路徑
- [ ] 我準備好學習並犯錯！

### 第一節課目標
- [ ] 成功執行第一個程式碼
- [ ] 下載真實的地震資料
- [ ] 建立地震圖
- [ ] 使用 AI 回答問題
- [ ] 完成至少一個練習

### 第一天結束時
- [ ] 熟悉 Google Colab
- [ ] 能夠下載和繪製地震資料
- [ ] 能夠應用基本濾波器
- [ ] 能夠有效使用 AI 工具
- [ ] 期待第二天！

---

## 🚦 狀態指標

**🟢 準備就緒**：您理解並可以繼續進行
**🟡 需要協助**：您遇到困難，請查看 [SETUP_GUIDE.md](SETUP_GUIDE.md) 或詢問 AI
**🔴 受阻**：技術問題，請詢問教師或開啟問題

---

## 🆘 獲得協助

### 自學期間
1. **查看** [QUICK_REFERENCE.md](QUICK_REFERENCE.md)
2. **詢問** Colab 中的 Gemini AI
3. **查詢** NotebookLM 您的問題
4. **檢閱** [SETUP_GUIDE.md](SETUP_GUIDE.md) 疑難排解章節
5. **搜尋** ObsPy 文件

### 上課期間
1. **詢問**助教
2. **與**夥伴合作
3. **舉手**請教老師
4. **詢問**鄰座同學

### 課後
1. **檢閱**課程資料
2. **在**討論區發文
3. **在**辦公時間電郵教師
4. **嘗試**使用 AI 協助的不同方法

---

## 🌟 成功故事

**「我從未編程過，卻在 10 分鐘內分析了我的第一個地震！」**
*- 首次編程者*

**「AI 輔助讓學習快得多。我可以專注於地震學，而不是語法。」**
*- 研究生*

**「我的學生整堂課都很投入。實作方法很有效！」**
*- 教師*

---

## 🎁 您將獲得什麼

### 立即
- ✅ 存取真實的地震資料
- ✅ 可運作的程式碼範例
- ✅ AI 學習助手
- ✅ 完整的文件

### 第一天後
- ✅ 實用的編程技能
- ✅ 地震學知識
- ✅ 繼續學習的信心
- ✅ 進階主題的基礎

### 長期
- ✅ 可轉移的 Python 技能
- ✅ AI 輔助學習能力
- ✅ 研究準備就緒
- ✅ 職業相關經驗

---

## 📖 建議閱讀順序

### 快速開始（30 分鐘）
1. 本檔案（GETTING_STARTED.md）
2. [QUICK_REFERENCE.md](QUICK_REFERENCE.md)
3. 開始使用 [first_day_tutorial.ipynb](first_day_tutorial.ipynb) 編程

### 完整理解（3 小時）
1. [README.md](README.md) - 概覽
2. [PROPOSAL.md](PROPOSAL.md) - 理念
3. [SETUP_GUIDE.md](SETUP_GUIDE.md) - 設定
4. [first_day_tutorial.ipynb](first_day_tutorial.ipynb) - 實作
5. [AI_PROMPTS_GUIDE.md](AI_PROMPTS_GUIDE.md) - AI 精通
6. [EXAMPLE_TUTORIAL.md](EXAMPLE_TUTORIAL.md) - 深入探討

### 給教師
1. [PROPOSAL.md](PROPOSAL.md) - 課程設計
2. [INSTRUCTOR_GUIDE.md](INSTRUCTOR_GUIDE.md) - 教學計畫
3. 所有學生資料 - 了解他們看到什麼
4. 自己測試所有內容

---

## 🎯 您的下一步

### 現在立即
1. 選擇上面的路徑
2. 開啟 Google Colab 或您偏好的環境
3. 執行您的第一個地震分析
4. 慶祝！🎉

### 本週
1. 完成 [first_day_tutorial.ipynb](first_day_tutorial.ipynb)
2. 嘗試所有挑戰練習
3. 探索不同的地震
4. 練習使用 AI 工具

### 本月
1. 在這些技能上繼續發展
2. 探索進階主題
3. 開始您自己的專案
4. 分享您所學到的

---

**準備好了嗎？選擇上面的路徑，讓我們開始您的地震學之旅！** 🌍📊🚀

---

*有問題嗎？開啟問題或聯絡課程教師。*
*覺得有幫助嗎？為儲存庫加星並與他人分享！*
