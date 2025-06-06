# 超級瑪莉歐 Web Demo

此專案使用 Python 與 Pygame 開發簡易的超級瑪莉歐風格遊戲，並透過 Pygbag 讓遊戲可以在瀏覽器中執行。

## 環境需求

- Python 3.10 以上
- `pygame`
- `flask`
- `pygbag` (將 Pygame 程式包裝成 WebAssembly)

安裝相依套件：

```bash
pip install -r requirements.txt
```

## 執行方式

1. 在開發環境中直接執行 `game.py` 可以於桌面模式遊玩：

```bash
python game.py
```

2. 若要在瀏覽器中遊玩，可先安裝 `pygbag` 並打包：

```bash
pygbag --build game.py
```

打包完成後會產生 `build/web` 目錄，啟動 Flask 伺服器：

```bash
python app.py
```

接著以瀏覽器開啟 `http://localhost:5000` 即可遊玩。

## 遊戲說明

- 方向鍵左右：移動
- 空白鍵：跳躍
- 角色碰到敵人即失敗
- 撿到香菇可以獲得加分

關卡長度不長，僅供示範使用。
