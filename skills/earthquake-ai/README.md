# Earthquake AI Skill

為 OpenClaw 設計的地震學 AI 助手技能，整合地震資料查詢、PyGMT 繪圖、Gemini AI 解釋、NotebookLM 教材生成、HuggingFace Space 部署等功能。

## 適用情境

- 大學與高中地震學課程的實作示範
- 教師快速產出地震快報與講義
- 研究初步資料探索與地震統計
- 防災教育活動的互動展示

## 安裝

```bash
# 1. 安裝技能
cd ~/.openclaw/workspace/skills
git clone https://github.com/oceanicdayi/earthquake-ai-skill.git earthquake-ai

# 2. 安裝依賴
cd earthquake-ai
npm install
npm run build

# 3. 讓 OpenClaw 載入
openclaw skills install ./earthquake-ai
```

## 環境變數

必需設定：

```bash
export GEMINI_API_KEY="your_gemini_api_key"
export HUGGINGFACE_TOKEN="your_hf_token"
```

可選：

```bash
export TAIGER_API_KEY="your_taiger_key"  # 台灣地震資料
```

OpenClaw 會自動繼承 `process.env` 中的變數，或在 `~/.openclaw/openclaw.json` 的 `env` 區段設定。

## 使用範例

### 1. 查詢地震並繪圖

```bash
openclaw agent --message "昨天台灣附近 M4.0 以上的地震有哪些？畫出分布圖。"
```

內部會執行：
- `usgs.fetch`（region=[119,123,21,26], minmagnitude=4.0）
- `pygmt.plot`（type='map'）

### 2. 生成教材

```bash
openclaw agent --message "請用 NotebookLM 風格生成『地震波傳播』的教材（中階程度）"
```

執行 `notebooklm.generate` 產生 Markdown 教材與測驗題。

### 3. 部署 Web App

```bash
openclaw agent --message "把地震查詢功能部署到 HuggingFace，名稱是 dayi-earthquake"
```

執行 `huggingface.deploy` 建立 Space 並提供範例 `app.py`。

### 4. 地震統計分析

```bash
openclaw agent --message "分析過去一週台灣地震的規模分布"
```

執行 `stats.analyze` + `usgs.fetch` 提供統計圖表。

### 5. 課堂即時問答

```bash
openclaw agent --message "學生問：『P 波和 S 波有什麼不同？』用圖表輔助解釋"
```

執行 `gemini.explain` 整合圖表與文字解釋。

## 工具一覽

| Tool | 功能 | 參數 |
|------|------|------|
| `usgs.fetch` | 取得 USGS 地震目錄 | `starttime`, `endtime`, `minmagnitude`, `region` |
| `pygmt.plot` | PyGMT 繪圖 | `type` (map/histogram/...), `data`, `region` |
| `gemini.explain` | AI 解釋 | `question`, `context`, `level` |
| `notebooklm.generate` | 生成教材 | `topic`, `level`, `includeQuiz` |
| `huggingface.deploy` | 部署 Space | `appType`, `name`, `appFile` |
| `stats.analyze` | 統計分析 | `data`, `metrics` |

## 資料品質與限制

- USGS 與 TAIGER 目錄更新速度會有數分鐘差異，課堂展示可先確認更新時間。
- 建議在繪圖前檢查 `region` 與 `starttime/endtime`，避免取得空資料或範圍錯置。
- 部署 Space 時請避免在公開程式碼中寫入 API 金鑰，改用 HuggingFace Secrets。

## Integration with OpenClaw

- **Cron jobs**：每天 9:00 自動執行 `usgs.fetch` + `pygmt.plot` + 發布到群組
- **Webhook**：接收地震即時預警，觸發 `gemini.explain`
- **Memory**：記錄學生的提問歷史，方便追蹤學習軌跡
- **Sub-agents**：可以派生獨立的地震分析 agent 處理大量數據

## Requirements

執行環境必需安裝：

```bash
pip install pygmt google-generativeai requests numpy pandas
```

## Troubleshooting

- `PyGMT 相關錯誤`：確保已安裝 `gmt` 系統套件 (Ubuntu: `apt install gmt`)
- `Gemini API 錯誤`：檢查 `GEMINI_API_KEY` 是否正確
- `Space 部署失敗`：確保 `HUGGINGFACE_TOKEN` 有 `write` 權限

## License

MIT
