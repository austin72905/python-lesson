import requests
from bs4 import BeautifulSoup
import re # 正則表達式庫

## 查找的方法
# .find_all(name,attrs,recurive,string,**kwargs)  返回的是一個list
# () 可以直接用這個方式簡寫

# 參數
# 1. name : 尋找tag的名稱
# 2. attrs : 尋找的屬性
# 3. recurive : 默認TRUE 是否對所有子孫節點的訊息搜索
# 4. string : 對 <>..</> 中間進行查找


## 擴充方法
#1. find 只返回一個結果 str
#2. find_parents 在先輩節點搜索 返回 list
#3. find_parent 在先輩節點搜索，只返回一個結果 str
#4. find_next_siblings 在後續平行節點搜索，返回 list
#5. find_next_sibling (同上邏輯)
#6. find_previous_siblings 返回 list
#7. find_previous_sibling


#### code region ####
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

# 返回都是列表
print(soup.find_all('a'))
print(soup.find_all(['a','b']))  # 可設定多個條件
print(soup.find_all(True)) # 顯示所有標籤

for tag in soup.find_all(True):
    print(tag.name)

# ex 以 b 開頭所有的要素
for tag in soup.find_all(re.compile('b')):
    print(tag.name)

# 有 course 這個屬性值的標籤
print(soup.find_all('p','course'))

# 找到  屬性id ='link1' 的標籤
print(soup.find_all(id='link1'))

# 需要找 包含link link1 時 (模糊查詢)，需要用正則庫
print(soup.find_all(id=re.compile('link1')))

# 對 <>..</> 中間進行查找
print(soup.find_all(string='Python'))

# 搭配正則庫，只要有Python 就會被找出來
print(soup.find_all(string=re.compile('Python')))

# ()簡寫
print(soup(string=re.compile('Python')))