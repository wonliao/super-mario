# Super Mario 遊戲 Demo

本專案是一個以經典《Super Mario Bros.》為靈感的 2D 平台遊戲示範。目標是透過多個 Agents 協作完成遊戲關卡、圖像與音效素材，以及基礎遊戲機制。詳細的 Agents 分工說明請參考 `AGENTS.md`。

## 目錄結構

```text
super-mario/
├── assets/    # 遊戲圖像與音效素材
├── engine/    # 物理與遊戲迴圈等核心邏輯
├── levels/    # 關卡配置檔
├── ui/        # HUD 與選單介面
├── main.py    # 遊戲進入點
└── AGENTS.md  # Agents 分工說明
```

## 執行方式

1. 確認已安裝 Python 3.x。
2. 在專案根目錄下執行：

```bash
python main.py
```

若日後需要安裝其他依賴，請依照 `requirements.txt` 或文件說明執行安裝。

## 開發流程或分工

各 Agent 的角色與任務已整理於 [`AGENTS.md`](./AGENTS.md)。開發者可根據文件說明參與關卡設計、素材繪製或程式開發。

