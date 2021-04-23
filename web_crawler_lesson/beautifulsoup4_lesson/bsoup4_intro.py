import requests
from bs4 import BeautifulSoup
#安裝指令 pip install beautifulsoup4

## 引入方式 
# from bs4 import BeautifulSoup
# import bs4

# 預設會轉換為utf-8

## 基本元素
# 可以用type 去查看他們的class

#1. Tag  標籤
#2. Name 標籤名                         <tag>.name
#3. Attribute 標籤屬性 (字典)            <tag>.attrs
#4. NavigableString 標籤包住的字串       <tag>.string (包住的標籤>2會打印none)   text (會打印拼接後的內容)
#5. Comment 註釋

## 解析器
#1. 'html.parser'
#2. 'lxml' 需安裝 pip install lxml
#3. 'xml'  同2
#4. 'html5lib' 需安裝 pip install html5lib


## 遍歷 HTML 結構

# 不只是Tag，NavigableString 也會被視為節點，所以需要判斷
#1. 下行遍歷
#2. 上行遍歷
#3. 平行遍歷

#方法
# 下行遍歷
#1. .content  子節點的列表，將<tag>所有子節點存入List   (只有下一層)
#2. .children 子節點迭代類型，與.content 相似，用於循環遍歷子節點  (只有下一層)
#3. .descendants 子孫節點的迭代類型，包含所有子孫節點，用於循環遍歷  (所有子孫)

# 上行遍歷
#1. .parent 節點的父親標籤
#2. .parents 節點的先輩們

# 平行遍歷
#需要在同個父節點下

#1. .next_sibling 按HTML文本順序的下一個平行節點
#2. .previous_sibling 按HTML文本順序的上一個平行節點
#3. .next_siblings 按HTML文本順序的後續所有平行節點
#4. .previous_siblings 按HTML文本順序的前面所有平行節點

## 美觀
#1. .prettify()  可針對某個TAG使用
#2. 預設會轉換為utf-8

#### code region ####
## 實際案例
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

print(soup.prettify())

## 基本元素
print("--------基本元素----------")
print(soup.title) # 獲取 <title>
print()
print(soup.a) # 獲取 a 標籤如果有多個會返回第一個

#2. Name 標籤名
print(soup.a.name)
print(soup.a.parent.name) # 包住a 的上一層標籤
print(soup.a.parent.parent.name)

#3. Attribute 標籤屬性 (字典)  
print(soup.a.attrs)
print(soup.a.attrs['href']) # 取得屬性字典的某個值

#4. NavigableString 標籤包住的字串
print(soup.a.string)

#5. Comment 註釋
newsoup = BeautifulSoup('<b><!--this is a comment--></b><p>oooo</p>','html.parser')

print(newsoup.b.string) # 就算是註釋他也看不出來
#需要藉助type
print(type(newsoup.b.string)) # <class 'bs4.element.Comment'>
print(newsoup.p.string)
print(type(newsoup.p.string)) # <class 'bs4.element.NavigableString'>

## 遍歷 HTML 結構
print("------ 遍歷 -------")
print(soup.head)
print(soup.body.contents)
print(len(soup.body.contents))
print(soup.body.contents[1])

# 下行遍歷的寫法
#for child in soup.body.children:
#    print(child)

#for child in soup.body.descendants:
#    print(child)

print("--------- 上行遍歷 ------------")
print(soup.title.parent) # <head><title>This is a python demo page</title></head>
# 上行遍歷的寫法
for parNode in soup.a.parents:
    if parNode is None: # soup 本身是沒有父節點的，會是none
        print(parNode)
    else:
        print(parNode.name)

print("--------- 平行遍歷 ------------")

print(soup.a.next_sibling) # 跟當前節點平行的 下一個節點
print("後續節點") # 跟當前節點平行的節點，及他的後續節點
for sibling in soup.a.next_siblings:
    print(sibling)

print("前續節點")
for sibling in soup.a.previous_siblings:
    print(sibling)
