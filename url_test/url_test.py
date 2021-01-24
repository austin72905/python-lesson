
#pip install requests 下載包
import requests
import time
import datetime

url ="http://localhost:56825/login"

headers ={"Content-type": "application/json"}

data = '{"username":"austin","password":"123"}'

#測試
count = 0
#timeNow = time.strftime('%Y-%m-%d',time.localtime())
today =datetime.date.today().strftime('%Y-%m-%d')

#從哪天開始刪
dayBefore =60
logName="payment-log."

#刪到哪天停止
while dayBefore<90:
    dayDelete=(datetime.date.today()-datetime.timedelta(dayBefore)).strftime('%Y-%m-%d')
    print(logName+dayDelete.replace("-","."))
    dayBefore+=1
    time.sleep(1)


#day30=(datetime.date.today()-datetime.timedelta(1)).strftime('%Y-%m-%d')
#print(day30.replace("-","."))

#while count<5:
    #resp =requests.post(url,headers=headers,data=data)
    #respData =resp.json()
    #print(respData["data"]["username"])
    #print(type(timeNow))
    #time.sleep(1)
    #count+=1

#resp =requests.post(url,headers=headers,data=data)

#respData =resp.json() # {'code': 0, 'data': {'username': 'austin', 'gender': '男', 'memberID': 1, 'isRegist': False}}
#print(respData["data"]["username"])