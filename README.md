# 超級瑪莉歐 Demo

這是一個使用 **Python** 與 **Pygame** 製作的簡易超級瑪莉歐風格遊戲。程式碼僅包含一個小關卡，適合作為展示用途。

## 執行方式
1. 安裝相依套件：
   ```bash
   pip install pygame
   ```
2. 執行遊戲：
   ```bash
   python mario_game.py
   ```

## 發佈為網頁版本
若要將遊戲包裝成網頁，可使用 [pygbag](https://github.com/pygame-web/pygbag)。安裝後執行：
```bash
pip install pygbag
pygbag --build mario_game.py
```
完成後會在 `build/web` 目錄產生可於瀏覽器遊玩的檔案。

## 操作說明
- 左右方向鍵：移動
- 空白鍵：跳躍

祝遊戲愉快！

## 圖片素材
請下載以下圖片並放入 `images` 目錄：
1. [靜止] https://static.wikia.nocookie.net/nintendo/images/d/d8/Mario_NSMBW.png/revision/latest/scale-to-width-down/1586?cb=20240314053054&path-prefix=en (儲存為 `mario.png`)
2. 跑步圖片 (`mario_run.png`)
3. 跳躍圖片 (`mario_jump.png`)

若沒有提供跑步或跳躍圖片，遊戲仍可執行，但角色將顯示為空白。
