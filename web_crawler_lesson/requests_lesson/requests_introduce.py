import requests


## requests 庫 7個主要方法

#1. request() 構造一個請求，支援以下方法的基礎方法 ()
#   (method,url,**args)

# **args
#1. params 值會放在querystring
#2. data 值會放在body
#3. json 值會放在body (json格式)
#4. headers
#5. cookies
#6. auth 元祖，支持HTTP認證功能
#7. file 傳輸文件
#8. timeout 超時時間 (秒)
#9. proxies 字典,設定訪問代理服務器，可以增加登陸功能
#10. allow_redirects: True/False 是否允許重定向
#11. stream: True/False 默認True，獲取內容立即下載
#12. verify: True/False 默認True，認證SSL證書
#13. cert: 本地SSL證書路徑


# 以下方法其實都是request()的封裝
#2. get()  get請求，構建一個Request對象， 返回一個 Response 對象
#3. head() 獲取 header
#4. post() post請求 data 帶dic 會以表單形式傳輸 帶 str 會被放在 data 字段
#5. put()  put 請求
#6. patch() patch 請求
#7. delete() delete 請求

## Response 對象

#1. status_code 響應碼
#2. headers 頭部訊息
#3. text 字串格式顯示頁面內容
#4. encoding 響應內容編碼方法(從header)
#5. apparent_encoding 從響應內容分析的編碼方式
#6. content 二進制形式顯示頁面內容

#7  request可以查看 可以查看request 相關訊息 ex: resp.request.headers

## 連接異常 ##
#req
#1. ConnectionError 如DNS查詢失敗、拒絕連接
#2. HTTPError HTTP錯誤異常
#3. URLRequired url缺失異常
#4. TooManyRedirects 超過最大重定向次數
#5. ConnectTimeout 遠程服務器超時異常
#6. Timeout 請求URL超時異常

#res
#7. raise_for_status() 如果不是200，產生HTTPError


## 通用代碼
def getHTMLText(url:str)->str:
    try:
        resp = requests.get(url,timeout=30)
        resp.raise_for_status() # 如果不是200 拋異常
        resp.encoding= resp.apparent_encoding
        return resp.text
    except:
        return "產生異常"
# 參見 namescope
if __name__ == "__main__":
    url ="https://www.google.com"
    #print(getHTMLText(url))



## 爬蟲規範

##服務器來源審查

#1. 檢查頭部的User-Agent，只響應瀏覽器或友好爬蟲

#2. Robots協議: 告知爬蟲協議(那些頁面可以爬)
#   =>網路爬蟲排除標準(根目錄下的robots.txt)

#語法
#1. User-agent 代表那些爬蟲
#2. Disallow 不可以訪問的目錄
#3. 無提供代表允許可爬

#如何遵守
#1. 爬蟲要能識別robots.txt，在進行爬取
#2. 建議但非約束性，但不遵守可能違法
#3. 如果訪問的數據量很小(類人類)，可不遵守


#### code region ####

## requests 庫 7個主要方法
#1. request()
resp = requests.request('GET',"https://www.google.com")

#requests.get("",params=None,**kwargs)

# **args
#7. file 傳輸文件
fs ={'file':open('test.txt','rb')}

#9. proxies
pxs ={ 'http':'http://user:pass@10.10.1:1234',
       'https' : 'https://10.10.10.1:4321'}


## Response 對象
resp1 = requests.get("https://www.google.com")

print(resp.status_code)
print(resp.headers) 
print(resp.encoding) # 不存在charset 字段，會莫認為 ISO-8859-1
print(resp.apparent_encoding) # 更加準確
#print(resp.content)
#resp.encoding = 'acsii'
#resp.raise_for_status()

## 連接異常 ##
requests.ConnectionError
requests.HTTPError
requests.URLRequired
requests.TooManyRedirects
requests.ConnectTimeout
requests.Timeout

