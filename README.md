# 轉盤抽獎機

此專案提供簡易的轉盤抽獎功能，使用 Python 與 Flask 架設後端，前端以 HTML/CSS/JavaScript 呈現。

## 環境需求
- Python 3.8 以上
- 套件依賴於 `requirements.txt`

## 安裝與執行
1. 安裝依賴：
   ```bash
   pip install -r requirements.txt
   ```
2. 啟動伺服器：
   ```bash
   python app.py
   ```
3. 於瀏覽器開啟 `http://localhost:5000` 即可看到轉盤介面。

## 紀錄檔位置與查詢
轉盤結果會以 JSON 形式逐行寫入 `spin_log.txt`，
可透過瀏覽 `http://localhost:5000/results` 取得目前的紀錄內容。

## 測試
執行以下指令進行測試：
```bash
python -m unittest discover tests
```
