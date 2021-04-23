import requests

# 從 google 搜索 youtube
def getHTMLText(url:str)->str:
    try:
        keyword={'q':'youtube'}
        resp =requests.get(url,params=keyword)
        print(resp.request.url)
        resp.raise_for_status()
        return resp.text[:1000]
    except:
        return "爬取失敗"

url= "https://www.google.com/search"
print(getHTMLText(url))
    