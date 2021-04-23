from bs4 import BeautifulSoup
import requests


# 尋找html 中所有 url
# 思路
# 1. 找到所有a 標籤
# 2. 取其中 href 的值

url = 'http://python123.io/ws/demo.html' # demo 網址

def getHTMLText(url:str)->str:
    try:
        resp =requests.get(url)
        resp.raise_for_status()
        resp.encoding =resp.apparent_encoding
        return resp.text
    except:
        return "爬取失敗"

content:str =getHTMLText(url)

# 建立一個 BeautifulSoup 對象
soup = BeautifulSoup(content,'html.parser')

# 思路
# 1. 找到所有a 標籤
# 2. 取其中 href 的值
for aTag in soup.find_all('a'):
    print(aTag.get('href'))