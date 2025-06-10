# Super Mario 遊戲 Demo

這是以 Python 撰寫的簡易 2D 平台遊戲範例，靈感來自經典《Super Mario Bros.》。

## 目錄結構

- `assets/`：遊戲所需的圖片與音效素材（目前以 `.gitkeep` 佔位）。
- `engine/`：遊戲主迴圈與物理引擎的實作。
- `levels/`：關卡資料，例如 `level_1.json`。
- `ui/`：包含 HUD 與選單等介面程式碼。
- `main.py`：啟動遊戲的入口點。
- `AGENTS.md`：說明各個協作 Agent 角色與分工。

## 執行方式

確保已安裝 Python 3，於專案根目錄執行：

```bash
python main.py
```

此版本僅提供最基本的迴圈與結構，可依需求擴充遊戲內容。

