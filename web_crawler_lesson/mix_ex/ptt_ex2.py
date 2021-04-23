import ptt_ex1
import bs4
import os
import re
import time
# 爬表特版 


#50 推以上的文章
# 標題含有奶 或 乳的
# 統計 作者 發文 質量

# 注意: 推文 爆 跟 X1 要處理

# tag.a 有時候會是None 要先判斷不是時，才打印

class Author:
    authorDic={}

    @classmethod
    def addAuthorToDic(cls,author:str):
        # 添加到作者字典
        if (author not in Author.authorDic.keys()):
            Author.authorDic.setdefault(author,1)
        else:
        # 該作者次數加一
            Author.authorDic[author]=Author.authorDic[author]+1

def printResult(taglist,filter1='',filter2='',filter3='',limit=0):
    linklist=[]
    for tag in taglist:
        pushCount = tag.find('div', 'nrec').text
        if matchCondition(tag,pushCount,filter1,filter2,filter3,limit):
            
            print()
            title = tag.a.string
            print(f"標題 :{title}")

            print(f"推數 : {pushCount}")

            link = tag.a.attrs['href']
            print(f"連結: {ptt_ex1.UrlInfo.baseUrl+link}")

            author = tag.find('div', 'author').string
            print(f"作者: {author}")

            print()
            print("**********")

            # 統計作者優文篇數
            Author.addAuthorToDic(author=author)
            # 將文章連結放入List
            linklist.append(ptt_ex1.UrlInfo.baseUrl+link)
    return linklist

# 過濾條件
def matchCondition(tag:bs4.element.Tag,pushCount:str,filter1:str,filter2:str,filter3:str,limit:int):
    # 規範只能是正整數
    match = re.search(r'^[0-9]*[1-9][0-9]*$|爆',pushCount)
    if match and (tag.a is not None):
        if(filter1 in tag.a.string or filter2 in tag.a.string or filter3 in tag.a.string):
            if pushCount == '爆':
                return True
            # 讚數要多少?
            return (int(pushCount)>limit)
    return False
            
def printAuthors(authorList):
    print('前五高質量發文')
    template='{0:<8}\t{1:^8}'
    print(template.format('作者','篇數'))
    # 取排名前5
    for item in authorList[0:5]:
        print(template.format(item[0],item[1]))

def main():
    url:str='https://www.ptt.cc/bbs/Beauty/index.html'
    rssion = ptt_ex1.createSession()
    # 從上頁的按鈕獲得目前數字
    depth = ptt_ex1.getArticleCount(url, rssion,'Beauty')
    # 爬取深度
    stop = depth - 200
    while (depth > stop):
        time.sleep(0.05)
        url = f'https://www.ptt.cc/bbs/Beauty/index{depth}.html'
        content: str = ptt_ex1.getHTMLText(url, rssion)
        if (content == 'error resp'):
            os._exit(0)
        templist: list = ptt_ex1.parseHtmlPage(content)
        printResult(templist,'奶','乳',limit=50)
        depth -= 1
        #print("************換頁*************")
    #print(Author.authorDic)
    # 按照value排序 (倒敘)
    authorList = sorted(Author.authorDic.items(),key=lambda d:-d[1])

    # 打印優文排行榜
    printAuthors(authorList)

if __name__=='__main__':
    main()

