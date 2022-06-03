import requests
import json
import pandas as pd
import time
import numpy as np

keyword = '衛生紙'
# 要抓取的網址
url = 'https://ecshweb.pchome.com.tw/search/v3.3/all/category/DAAG/results?q='+keyword+'&page=1&sort=sale/dc'
#請求網站
list_req = requests.get(url)
#將整個網站的程式碼爬下來
getdata = json.loads(list_req.content)

# 蒐集多頁的資料，打包成csv檔案
alldata = pd.DataFrame() # 準備一個容器
for i in range(1,2):
    # 要抓取的網址
    url = 'https://ecshweb.pchome.com.tw/search/v3.3/all/category/DAAG/results?q='+keyword+'&page='+str(i)+'&sort=sale/dc'
    #請求網站
    list_req = requests.get(url)
    #將整個網站的程式碼爬下來
    getdata = json.loads(list_req.content)
    todataFrame = pd.DataFrame(getdata['prods']) # 轉成Dataframe格式

    #Add pares key word
    # print(todataFrame[E:G])
    alldata.loc["E":"G"]
    #alldata.loc["name":"price"]
    #alldata = pd.DataFrame(np.arange(1, 66).reshape((22, 3)), columns=["name","describe","price"])
    #alldata = pd.DataFrame([np.alldata(), todataFrame[E:G]]) # 將結果裝進容器
    #paseData=todataFrame["name","describe","price"]
    #alldata = pd.DataFrame([np.alldata(), paseData[]) # 將結果裝進容器
    
    time.sleep(5) #拖延時間

# 儲存檔案
alldata.to_csv('PChome.csv', # 名稱
               encoding='utf-8-sig', # 編碼 
               index=False) # 是否保留Indexn
