# GoBus
```
GoBus 是一個提醒公車來了沒有的小工具，只要設定好資料，便可以顯示公車還有多久會來
```

## 適用範圍
```
1. 大台北地區
2. 資料來源： 5284
```

## 如何使用
```
1. 去 5284 找出想要搭乘的路線，ex: http://pda.5284.com.tw/MQS/businfo2.jsp?routename=930
2. 在瀏覽器中選擇觀看網頁原始檔
3. 依序複製紅框處 2 行字串，第 2 個字串前後需包含 "<" and ">"
```
![page content](/image/5284.png)
```
4. 將相關資訊儲存於 GoBus.json
5. 如果是想要提醒公車來了，該下班了，可以設定工作排程器，每天固定時間提醒
```

## 執行畫面
![running](/image/gobus.png)

## 使用語言
```
Python
```

## 額外模組
```
1. wxPython
2. requests
```



