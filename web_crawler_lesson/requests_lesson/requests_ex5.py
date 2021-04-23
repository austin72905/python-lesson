import requests

# 解析IP
# 去 ip138 網站 查看 查詢ip 時的 querystring

url = 'https://www.ip138.com/iplookup.asp'

def getHTMLText(url:str)->str:
    try:
        headers={'User-Agent':'Mozilla/5.0'}
        params ={'ip':'49.218.6.185','action':'2'}
        resp = requests.get(url,headers=headers,params=params)
        resp.raise_for_status()
        resp.encoding =resp.apparent_encoding
        return resp.text
    except:
        return "爬取異常"

content = getHTMLText(url)
print(content[1000:2000])