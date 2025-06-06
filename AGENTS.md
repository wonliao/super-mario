以下是一份針對開發「Super Mario 遊戲 demo」的 `AGENTS.md` 文件範例，適用於說明在多人協作或 AI 協作開發流程中，各個 Agent 的角色與任務分工。

---

# 🧠 AGENTS.md

本文件說明開發 Super Mario 遊戲 Demo 所使用之各個 Agent 的角色與分工，協助開發流程協調與模組化。

---

## 🎮 專案簡介

本專案為一個 2D 平台遊戲 Demo，致敬經典《Super Mario Bros.》，具備基本功能如玩家移動、跳躍、敵人碰撞、關卡設計與音效。

---

## 🤖 Agents 角色定義

### 1. `GameDesignerAgent`

* **目的**：規劃遊戲關卡流程與角色設計
* **任務**：

  * 設計關卡地形（例如起始點、終點、平台、障礙物）
  * 定義敵人類型與出現位置
  * 協調遊戲節奏與難度平衡
* **輸出**：JSON 或 YAML 格式的關卡配置檔 `levels/level_1.json`

---

### 2. `GraphicsAgent`

* **目的**：產出遊戲中使用的像素風格圖像素材
* **任務**：

  * 設計角色、敵人、場景、背景等美術資源
  * 優化圖檔以利載入與效能
* **輸出**：`assets/characters/`, `assets/backgrounds/`, `assets/tilesets/` 中的圖像資源 (PNG)

---

### 3. `AudioAgent`

* **目的**：製作並整合音效與背景音樂
* **任務**：

  * 製作背景音樂（例如：進行曲、勝利音樂）
  * 設計音效（跳躍、踩敵人、死亡）
* **輸出**：`assets/audio/` 下的 MP3/WAV 音效檔

---

### 4. `PhysicsAgent`

* **目的**：負責角色移動與碰撞邏輯
* **任務**：

  * 建立重力、跳躍、移動邏輯
  * 撰寫地圖磚塊與角色的碰撞邏輯
  * 支援平台碰撞、敵人互動
* **輸出**：`engine/physics.py`

---

### 5. `UIAgent`

* **目的**：負責介面與 HUD 元件
* **任務**：

  * 製作生命條、得分顯示、開始/結束畫面
  * 提供遊戲暫停與重新開始功能
* **輸出**：`ui/hud.py`, `ui/menu.py`

---

### 6. `IntegrationAgent`

* **目的**：協調其他 Agent 的產出並進行整合
* **任務**：

  * 將美術、音效、邏輯整合至主遊戲流程
  * 管理資源載入與初始化邏輯
  * 撰寫 `main.py`，作為遊戲進入點
* **輸出**：`main.py`, `engine/game_loop.py`

---

## 📁 專案目錄結構（簡要）

```
super-mario-demo/
├── assets/
│   ├── audio/
│   ├── backgrounds/
│   ├── characters/
│   └── tilesets/
├── engine/
│   ├── physics.py
│   └── game_loop.py
├── levels/
│   └── level_1.json
├── ui/
│   ├── hud.py
│   └── menu.py
├── main.py
└── AGENTS.md
```

---

## 🚀 運作流程建議

1. `GameDesignerAgent` 先提供關卡初稿
2. `GraphicsAgent` 和 `AudioAgent` 提供必要素材
3. `PhysicsAgent` 撰寫角色互動邏輯
4. `UIAgent` 設計 HUD 與遊戲流程畫面
5. `IntegrationAgent` 統整所有模組，執行整合測試

---

如需依需求新增 Agent（如 AI 敵人、多人連線等），請更新本文件並通知團隊成員。


