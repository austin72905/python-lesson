import requests
import bs4
import re
import os
import time
from enum import IntEnum

# 保持登入狀態
def createSession() -> requests.session:
    
    # 跨請求地保持某些引數
    rssion = requests.session()
    rssion.post(PttInfo.askO18Url, data=PttInfo.askOver18, headers=PttInfo.headers)
    return rssion

class PttInfo:
    baseUrl :str = 'https://www.ptt.cc'
    #over18
    askO18Url :str = f'{baseUrl}/ask/over18'
    headers :dict = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    askOver18 = {'from': '/bbs/Gossiping/index.html', 'yes': 'yes'}

    # 所有爬取過的文章
    allArtlist=[]

    #發文者字典
    authorDic = {}

    # 每篇文章內文資訊 列表
    contentInfoList = []

    # 推文者 id 字典
    pushIdDic = {}


class Article:
    def __init__(self,title,link,author,pushCount):
        self.title = title
        self.link = link
        self.author = author
        self.pushCount= pushCount

class Content:
    def __init__(self,title,author,ip,push):
        self.title = title
        self.author = author
        self.ip = ip
        # 推文list
        self.push = push

class Sort(IntEnum):
    KEY = 1
    VALUE = 2

class ArticleFilter(IntEnum):
    TITLE = 1
    AUTHOR = 2
    LINK = 3

class ContentFilter(IntEnum):
    CONTENT = 1
    IP = 2
    USERID = 3
    COMMENT = 4


class Pttcrawler:

    rssion = createSession()

    articleFiter =ArticleFilter.TITLE

    contentFilter =ContentFilter.COMMENT

    
    def __init__(self,board,depth=0):
        url = PttInfo.baseUrl+ f'/bbs/{board}/index.html'
        self.board = board
        self.depth = depth      
        self.nowDepth = getArticleCount(url, Pttcrawler.rssion,board)
        # 所有文章
        self.allArtlist = []
        # 發文者
        self.authorDic = {}
        # 推文
        self.pushIdDic = {}
        # 所有內文
        self.contentInfoList=[]

    def sort(self,sortDic,key=-Sort.VALUE):
        pushCList = []
        if key == -Sort.VALUE:
            pushCList = sorted(sortDic.items(),key=lambda d:-d[1])
        elif key == Sort.VALUE:
            pushCList = sorted(sortDic.items(),key=lambda d:-d[1])
        elif key == -Sort.KEY:
            pushCList = sorted(sortDic.items(),key=lambda d:-d[0])
        else :
            pushCList = sorted(sortDic.items(),key=lambda d:d[0])
        
        return pushCList

    def parseArticlePage(self,limit = 0,*filters,**other):
        # 是否立即打印
        printNow =False

        if 'printNow' in other.keys():
            printNow=True

        if ('url' in other.keys()):
            url = other['url']
            articleList = self.parseArticle(url,limit,printNow,*filters)
            return articleList
        elif ('search' in other.keys()):
            url = PttInfo.baseUrl+f'/bbs/{self.board}/search?q='+other['search']
            articleList = self.parseArticle(url,limit,printNow,*filters)
            return articleList

   
        nowDepth =self.nowDepth
        stop =self.nowDepth - self.depth
        while (nowDepth >= stop):
            time.sleep(0.05)
            url = PttInfo.baseUrl+f'/bbs/{self.board}/index{nowDepth}.html'
            articleList = self.parseArticle(url,limit,printNow,*filters)
            nowDepth -= 1
        
        return self.allArtlist

    
    def parseArticle(self,url,limit,printNow,*filters):
        articleList = self.parseToArtitleList(url,Pttcrawler.rssion,limit,*filters)
        # 立即打印
        if printNow:
            printResult(articleList)
        return articleList


    

    # 把重複的動作濃縮
    def parseToArtitleList(self,url:str,rssion,limit=0,*filters):
        content: str = getHTMLText(url,rssion)
        if (content == 'error resp'):
            os._exit(0)
        # 爬取文章列表
        articleList: list = parseArticlePage(content,limit,*filters)
        #將爬取過的文章加入allArtlist
        self.allArtlist = self.allArtlist + articleList
        #作者字典
        self.getGoodPostRank(articleList)
        return articleList


    def getGoodPostRank(self,articleList):
        for article in articleList:
            # 添加到作者字典
            if (article.author not in self.authorDic.keys()):
                self.authorDic.setdefault(article.author,1)
            else:
            # 該作者次數加一
                self.authorDic[article.author]=self.authorDic[article.author]+1
        return self.authorDic

    # 打印作者
    def printAuthors(self,sortList,score,ranktitle,col1,col2):
        if score > len(sortList) or score == 0:
            score = len(sortList)
        print(ranktitle)
        template='{0:<8}\t{1:^8}'
        print(template.format(col1,col2))
        # 取排名前5
        for item in sortList[0:score]:
            print(template.format(item[0],item[1]))

    
    def parseContentPage(self,*filters,**other): 

        # 直接爬內文
        if ('url' in other.keys()):
            url = other['url']
            content= getHTMLText(url, Pttcrawler.rssion)
            if (content == 'error resp'):
                print("err")
                os._exit(0)
            # 內文資訊
            contentInfo = parseContentPage(content,*filters)
            if contentInfo is not None:
                self.contentInfoList.append(contentInfo)
        else:
            # 爬內文
            for article in self.allArtlist:
                content= getHTMLText(article.link, Pttcrawler.rssion)
                if (content == 'error resp'):
                    print("err")
                    os._exit(0)
                # 內文資訊
                contentInfo = parseContentPage(content,*filters)
                if contentInfo is not None:
                    self.contentInfoList.append(contentInfo)
        return self.contentInfoList

    # 推文數量排名
    def getPushRank(self):
        for content in self.contentInfoList:
            for comment in content.push:
                # 添加到作者字典
                if (comment[0] not in self.pushIdDic.keys()):
                    self.pushIdDic.setdefault(comment[0],1)
                else:
                # 該作者次數加一
                    self.pushIdDic[comment[0]]=self.pushIdDic[comment[0]]+1
        return self.pushIdDic

    def printComment(self,authorList=None,score=5,origin=False):

        # 打印每篇所有留言
        if origin:
            for content in self.contentInfoList:
                for pm in content.push:
                    print(pm[0] +' '+ pm[1])
                print()
                print("*****"+ content.title +"*****")
                print("*****"+ content.author +"*****")
                print()
            return
            
        if score > len(authorList):
            score = len(authorList)
        

        for author in authorList[0:score]:
            print()
            print(f'----------{author[0]} 留言----------')
            print()
            for content in self.contentInfoList:
                apushcot=0
                for pm in content.push:
                    if pm[0] == author[0]:
                        apushcot+=1
                        print(pm[1])
                # 該作者有推文過的標題再打印
                if(apushcot>0):
                    print()
                    print("*****"+ content.title +"*****")
                    print("*****"+ content.author +"*****")
                    print()





def getHTMLText(url: str, rssion: requests.session) -> str:
    try:
        resp = rssion.get(url, headers=PttInfo.headers)
        resp.raise_for_status()
        resp.encoding = resp.apparent_encoding
        return resp.text
    except:
        print("url: "+url)
        print("request: "+resp.request)
        print("響應: "+resp.status_code)
        return "error resp"

# 獲取文章數量
def getArticleCount(url: str, rssion: requests.session,board:str):
    content = getHTMLText(url, rssion)
    soup = bs4.BeautifulSoup(content, 'html.parser')
    for tag in soup.find('div', re.compile(r'btn-group-paging')).children:
        if isinstance(tag, bs4.element.Tag):
            # 篩選出裡面有 ['r-ent'] 屬性的tag
            # <a class="btn wide" href="/bbs/Gossiping/index38858.html">‹ 上頁</a>
            if (tag.string == '‹ 上頁'):
                depth = re.sub(r'/bbs/{0}/index|.html'.format(board), '',
                               tag.attrs['href'])
                #print(depth)
                return int(depth)

def parseArticlePage(content: str,limit=0,*filters) -> list:
        
    soup = bs4.BeautifulSoup(content, 'html.parser')

    taglist = []
    for tag in soup.find('div', re.compile(r'r-list')).children:
        if isinstance(tag, bs4.element.Tag):
            # 篩選出裡面有 ['r-ent'] 屬性的tag
            if (['r-ent'] in tag.attrs.values() and (tag.a is not None)):
                pushCount = tag.find('div', 'nrec').text
                title = tag.a.text
                link = tag.a.attrs['href']
                author = tag.find('div', 'author').text
                if (Pttcrawler.articleFiter == ArticleFilter.TITLE):
                    filterStr = title
                elif (Pttcrawler.articleFiter == ArticleFilter.AUTHOR):
                    filterStr = author
                elif (Pttcrawler.articleFiter == ArticleFilter.LINK):
                    filterStr = link
                
                # 之後改成過濾條件
                if matchCondition(filterStr,pushCount,limit,*filters):               
                    taglist.append(Article(title,PttInfo.baseUrl+link,author,pushCount))
    return taglist


# 解析內文
def parseContentPage(content: str,*filters) -> Content:  
    infoList=[]
    push=[]
    ip=''
    soup = bs4.BeautifulSoup(content, 'html.parser')

    for tag in soup.find('div', id=re.compile(r'main-content')).children:
        
        if isinstance(tag, bs4.element.Tag):
            attrsVals = tag.attrs.values()
            if(['f2'] in attrsVals): 
                # ip
                if  tag.text.startswith('※ 發信站:'):       
                    ip = tag.text
                ip = ip.replace('※ 發信站: 批踢踢實業坊(ptt.cc), 來自:','').replace('\n','')
                if(Pttcrawler.contentFilter == ContentFilter.IP):
                    if not matchComCondition(ip,*filters):
                        return
                
            elif (['push'] in attrsVals):
                # 推文
                userid = tag.find('span',re.compile(r'push-userid')).text
                comment = tag.find('span',re.compile(r'push-content')).text
                # tuple
                pushFilter = filters
                if (Pttcrawler.contentFilter == ContentFilter.COMMENT):
                    filterStr = comment
                elif (Pttcrawler.contentFilter == ContentFilter.USERID):
                    filterStr = userid
                else:
                    filterStr = comment
                    pushFilter =()
                # print(userid)
                # print(comment)
                # 過濾條件
                if matchComCondition(filterStr,*pushFilter):
                    push.append((userid,comment))
            elif(['article-metaline'] in attrsVals):
                # 作者、標題、時間
                infoList.append(tag.find('span',re.compile(r'article-meta-value')).string)

    if infoList:
        author= infoList[0]
        title = infoList[1]
    else:
        author = ''
        title=''

    return Content(title,author,ip,push)

# 過濾條件
def matchCondition(compareStr:str,pushCount:str,limit:int,*filters):
    compareStr = compareStr if compareStr is not None else ''
    # 規範只能是正整數
    match = re.search(r'^[0-9]*[1-9][0-9]*$|爆',pushCount)
    if match :
        # 將 過濾參數以list 保存
        # 判斷 標題是否含有過濾參數的字串
        # [] 會被判斷為false
        filterList = [f for f in filters if f in compareStr]
        if filterList or not filters:
            if pushCount == '爆':
                return True
            # 讚數要多少?
            return (int(pushCount)>limit)
    return False

# 過濾推文條件
def matchComCondition(compareStr:str,*filters):
    compareStr = compareStr if compareStr is not None else ''
    # 將 過濾參數以list 保存
    # 判斷 標題是否含有過濾參數的字串
    # [] 會被判斷為false
    filterList = [f for f in filters if f in compareStr]
    if filterList or not filters:
        return True
    return False



# 優文數量排名
def getGoodPostRank(articleList):
    for article in articleList:
        # 添加到作者字典
        if (article.author not in PttInfo.authorDic.keys()):
            PttInfo.authorDic.setdefault(article.author,1)
        else:
        # 該作者次數加一
            PttInfo.authorDic[article.author]=PttInfo.authorDic[article.author]+1
    return PttInfo.authorDic

# 推文數量排名
def getPushRank():
    for content in PttInfo.contentInfoList:
        for comment in content.push:
            # 添加到作者字典
            if (comment[0] not in PttInfo.pushIdDic.keys()):
                PttInfo.pushIdDic.setdefault(comment[0],1)
            else:
            # 該作者次數加一
                PttInfo.pushIdDic[comment[0]]=PttInfo.pushIdDic[comment[0]]+1
    return PttInfo.pushIdDic


def printResult(taglist):
    for article in taglist:
            print()
            print(f"標題 :{article.title}")
            print(f"推數 : {article.pushCount}")
            print(f"連結: {article.link}")           
            print(f"作者: {article.author}")
            print()
            print("**********")

# 打印作者
def printAuthors(authorList,ranktitle,col1,col2):
    print(ranktitle)
    template='{0:<8}\t{1:^8}'
    print(template.format(col1,col2))
    # 取排名前5
    for item in authorList[0:5]:
        print(template.format(item[0],item[1]))

def printComment(authorList):

    for author in authorList[0:5]:
        print()
        print(f'----------{author[0]} 留言----------')
        print()
        for content in PttInfo.contentInfoList:
            apushcot=0
            for pm in content.push:
                if pm[0] == author[0]:
                    apushcot+=1
                    print(pm[1]) # 留言內容
            # 該作者有推文過的標題再打印
            if(apushcot>0):
                print()
                print("*****"+ content.title +"*****")
                print("*****"+ content.author +"*****")
                print()



def main():
    board='Beauty'
    url = PttInfo.baseUrl+ f'/bbs/{board}/index.html'
    rssion = createSession()
    # 從上頁的按鈕獲得目前數字
    depth = getArticleCount(url, rssion,board)
    # 爬取深度
    stop = depth - 10

    while (depth > stop):
        time.sleep(0.05)
        url = PttInfo.baseUrl+f'/bbs/{board}/index{depth}.html'
        content: str = getHTMLText(url, rssion)
        if (content == 'error resp'):
            os._exit(0)
        # 爬取文章列表
        articleList: list = parseArticlePage(content,10,'正妹')
        #將爬取過的文章加入allArtlist
        PttInfo.allArtlist = PttInfo.allArtlist + articleList
        printResult(articleList)
        #作者字典
        getGoodPostRank(articleList)
        depth -= 1

    # 發文者
    authorList = sorted(PttInfo.authorDic.items(),key=lambda d:-d[1])
    # 打印優文排行榜
    printAuthors(authorList,'前五優文排行','作者','篇數')

    
    # 爬內文
    for article in PttInfo.allArtlist:
        content= getHTMLText(article.link, rssion)
        if (content == 'error resp'):
            print("err")
            os._exit(0)
        # 內文資訊
        contentInfo = parseContentPage(content,'大')
        PttInfo.contentInfoList.append(contentInfo)

    # 統計某些帳號的推文數
    pushIdDic= getPushRank()

    # 所有推文者字典
    pushCList= sorted(pushIdDic.items(),key=lambda d:-d[1])
    # 打印優文排行榜
    printAuthors(pushCList,'前五推文排行','推文id','推文數')
    printComment(pushCList)

def main2():
    pttObj = Pttcrawler('Beauty',100)
    printNow = {'printNow':True,'url':''}
    pttObj.parseArticlePage(10,'奶',**printNow)
    # 發文者
    authorList = sorted(pttObj.authorDic.items(),key=lambda d:-d[1])
    # 打印優文排行榜
    pttObj.printAuthors(authorList,5,'前五優文排行','作者','篇數')

    # 解析內文
    pttObj.parseContentPage('大')
    pushIdDic = pttObj.getPushRank()
    # 推文者
    pushCList = sorted(pushIdDic.items(),key=lambda d:-d[1])
    # 打印優文排行榜
    pttObj.printAuthors(pushCList,5,'前五推文排行','推文id','推文數')
    pttObj.printComment(pushCList)

def main3():
    time1 = time.time()
    # 待完成
    # https://www.ptt.cc/bbs/Beauty/search?q=[正妹]
    # 創建一個爬ptt 的實例
    pttObj = Pttcrawler(board='Gossiping',depth=100)

    # 可以直接 輸入url 爬取該頁面
    # printNow = {'printNow':True,'url':'https://www.ptt.cc/bbs/home-sale/index5014.html'}
    printNow = {'printNow':True} # ,'search':'[正妹] 母愛'

    #Pttcrawler.articleFiter=ArticleFilter.AUTHOR
    # 爬取文章列表
    pttObj.parseArticlePage(0,'柯','台鐵','李義祥',**printNow)# **printNow

    time2 = time.time()
    # 發文者
    #authorList = sorted(pttObj.authorDic.items(),key=lambda d:-d[1])
    authorList = pttObj.sort(pttObj.authorDic)
    # 打印優文排行榜
    pttObj.printAuthors(authorList,5,'前五優文排行','作者','篇數')

    Pttcrawler.contentFilter=ContentFilter.USERID
    # 爬取內文
    pttObj.parseContentPage()

    time3 = time.time()

    # 取得推文最多的用戶id
    #pushIdDic= pttObj.getPushRank()

    time4 = time.time()
    # 按次數排序
    #pushCList = sorted(pushIdDic.items(),key=lambda d:-d[1])
    #pushCList = pttObj.sort(pushIdDic)
    # 打印優文排行榜
    #pttObj.printAuthors(pushCList,5,'前十推文排行','推文id','推文數')

    # 打印 留言
    pttObj.printComment(origin=True)

    time5 = time.time()

    print('爬取文章耗時')
    print(time2-time1)
    print("爬取內文耗時")
    print(time3-time2)
    print("取得推文最多的用戶id耗時")
    print(time4-time3)
    print("打印留言耗時")
    print(time5-time4)

def main4():
    time1 = time.time()
    time.sleep(5)
    time2 = time.time()

    print(time2-time1)

if __name__=='__main__':
    main3()

