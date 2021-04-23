import requests

url='https://www.amazon.com/dp/B08SQMTB52/ref=sr_1_1_sspa?adgrpid=81256009653&dchild=1&gclid=CjwKCAjwr_uCBhAFEiwAX8YJgW1qVIF69bT0lI0HiKVq3jhRc17agzrkFNXfJdJ1AIrBkGfPG8g7nxoC2X0QAvD_BwE&hvadid=393559199195&hvdev=c&hvlocphy=9040380&hvnetw=g&hvqmt=b&hvrand=15580810167186197237&hvtargid=kwd-26342230&hydadcr=21587_10785041&keywords=amazon&qid=1616854458&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFQWTNTOFlROFMxUUkmZW5jcnlwdGVkSWQ9QTAwMTg1NjUxNUNOWFVZQ1ZEUElRJmVuY3J5cHRlZEFkSWQ9QTAwNDg4MTVOQUFUUFQ1RFVYV00md2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl'

resp = requests.get(url)
# 有些網站會檔爬蟲，可以試著 修改 User-Agent
# Mozilla/5.0
# 亞馬遜很會檔ㄏㄏ，還是會失敗
print(resp.request.headers) #{'User-Agent': 'python-requests/2.25.1', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
print()
print("******* 改良版 ********")

def getHTMLText(url:str):
    try:
        headers = {'User-Agent':'Mozilla/5.0'}
        resp2 = requests.get(url,headers=headers,timeout=30)
        print(resp2.request.headers)
        resp2.raise_for_status()
        resp2.encoding = resp2.apparent_encoding
        return resp2.text[1000:2000]
    except:
        return "爬取異常"

print(getHTMLText(url))

