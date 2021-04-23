import requests
import ptt_ex1
import ptt_ex2
import os
import bs4
import re
import time

# url='https://www.books.com.tw/products/0010887358?loc=P_0025_1_001'

# def getHTMLText(url: str) -> str:
#     try:
#         headers = {
#             'User-Agent':
#             'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
#             ,
#             'HTTP_CLIENT_IP':
#             '127.0.0.1'
#         }
#         resp = requests.get(url, headers=headers,stream=True)
#         #resp.raise_for_status()
#         #resp.encoding = resp.apparent_encoding
#         #resp.raw._connection.sock.getpeername()[0]
#         return resp.raw._connection.sock.getsockname()[0]
#     except:
#         return "error resp"


# ptt 內文的打印

# 找出標題的關鍵字
# 含有台鐵、李義祥
# 打印那些文
# 進去內文(href)
# dict統計回文的人

def parseHtmlPage(content: str) -> list:
    soup = bs4.BeautifulSoup(content, 'html.parser')

    taglist = []
    for tag in soup.find('div', id=re.compile(r'main-content')).children:
        if isinstance(tag, bs4.element.Tag):
            # 篩選出裡面有 ['r-ent'] 屬性的tag
            if (['push'] in tag.attrs.values()):
                taglist.append(tag)
    return taglist



def printResult(taglist):
    for tag in taglist:
        userid = tag.find('span',re.compile(r'push-userid')).string
        commend = tag.find('span',re.compile(r'push-content')).string
        if(userid=='terry1043'):
            print("留言 " + commend)

        # 統計作者優文篇數
        ptt_ex2.Author.addAuthorToDic(author=userid)
        #print(userid)
        #print(userid+"   "+commend)



def main():
    url :str= 'https://www.ptt.cc/bbs/LoL/index.html'
    rssion = ptt_ex1.createSession()
    # 從上頁的按鈕獲得目前數字
    depth = ptt_ex1.getArticleCount(url, rssion,'LoL')
    # 爬取深度
    stop = depth - 100
    while (depth > stop):
        time.sleep(0.05)
        url = f'https://www.ptt.cc/bbs/LoL/index{depth}.html'
        content: str = ptt_ex1.getHTMLText(url, rssion)
        if (content == 'error resp'):
            print("err")
            os._exit(0)
        # 看板文章列表
        taglist = ptt_ex1.parseHtmlPage(content)
        linkList=ptt_ex2.printResult(taglist,'','','',limit=10)
        depth -= 1
    
    for link in linkList:
        content= ptt_ex1.getHTMLText(link, rssion)
        if (content == 'error resp'):
            print("err")
            os._exit(0)
        # 內文推數
        taglist=parseHtmlPage(content)
        printResult(taglist)
    
    authorList = sorted(ptt_ex2.Author.authorDic.items(),key=lambda d:-d[1])

    # 打印優文排行榜
    ptt_ex2.printAuthors(authorList)
    
    



    
    


if __name__=='__main__':
    main()
