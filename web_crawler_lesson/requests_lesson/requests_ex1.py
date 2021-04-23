import requests

def getHTMLText(url:str):
    try:
        resp = requests.get(url,timeout=30)
        resp.raise_for_status()
        resp.encoding = resp.apparent_encoding
        return resp.text[:1000]
    except:
        return "爬取異常"

url:str ="https://www.books.com.tw/products/0010887358?loc=P_0025_1_001"

print(getHTMLText(url))