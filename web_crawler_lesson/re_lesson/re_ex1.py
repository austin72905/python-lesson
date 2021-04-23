import re
import requests
import bs4

## momo爬蟲

# 獲取搜尋頁面的訊息，取得商品名、價格
# 有分頁


# 動態網頁 去 network 看 preview 可以找到response 

# 實際抓取資料的url
# https://www.momoshop.com.tw/ajax/ajaxTool.jsp?n=2018&t=1617465136853
# t 當前時間戳


def getHTMLText(url:str)->str:
    try:
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
        #params ={'ip':'49.218.6.185','action':'2'}
        resp = requests.get(url,headers=headers)
        resp.raise_for_status()
        resp.encoding =resp.apparent_encoding
        return resp.text
    except:
        return "爬取異常"

keyword='筆電'
lengh ='2'
url = f'https://www.momoshop.com.tw/search/searchShop.jsp?keyword={keyword}&searchType=1&cateLevel=0&curPage=1&_isFuzzy=0'
print(url)
content = getHTMLText(url)

soup = bs4.BeautifulSoup(content,'html.parser')

for tag in soup.find_all('div','listArea'):
    print(tag)
