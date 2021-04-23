import requests
import bs4
import re
import os

## 爬八卦版

# session 應用
# https://www.itread01.com/content/1547547303.html

# 進八卦板前 會問 是否滿18

class UrlInfo:
    baseUrl:str = 'https://www.ptt.cc'
    board:str = '/bbs/Gossiping/index.html'

def createSession() -> requests.session:
    #over18
    askO18Url = 'https://www.ptt.cc/ask/over18'
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    askOver18 = {'from': '/bbs/Gossiping/index.html', 'yes': 'yes'}
    # 跨請求地保持某些引數
    rssion = requests.session()
    rssion.post(askO18Url, data=askOver18, headers=headers)
    return rssion


def getHTMLText(url: str, rssion: requests.session) -> str:
    try:
        headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
        }
        resp = rssion.get(url, headers=headers)
        resp.raise_for_status()
        resp.encoding = resp.apparent_encoding
        return resp.text
    except:
        print("請求鏈結: "+resp.request)
        print("響應: "+resp.status_code)
        return "error resp"


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


def parseHtmlPage(content: str) -> list:
    soup = bs4.BeautifulSoup(content, 'html.parser')

    taglist = []
    for tag in soup.find('div', re.compile(r'r-list')).children:
        if isinstance(tag, bs4.element.Tag):
            # 篩選出裡面有 ['r-ent'] 屬性的tag
            if (['r-ent'] in tag.attrs.values()):
                taglist.append(tag)
    return taglist


def printResult(taglist):
    for tag in taglist:
        if (tag.a is not None):
            print()
            title = tag.a.string
            print(f"標題 :{title}")

            link = tag.a.attrs['href']
            print(f"連結: {UrlInfo.baseUrl+link}")

            author = tag.find('div', 'author').string
            print(f"作者: {author}")

            print()
            print("**********")


def main():
    # 將登入訊息保存
    rssion = createSession()
    url: str = 'https://www.ptt.cc/bbs/Gossiping/index.html'

    # 從上頁的按鈕獲得目前數字
    depth = getArticleCount(url, rssion,'Gossiping')
    # 爬取深度
    stop = depth - 2
    while (depth > stop):
        url = f'https://www.ptt.cc/bbs/Gossiping/index{depth}.html'
        content: str = getHTMLText(url, rssion)
        if (content == 'error resp'):
            os._exit(0)
        templist: list = parseHtmlPage(content)
        printResult(templist)
        depth -= 1
        print("************換頁*************")



# 執行主程式
if __name__=='__main__':
    main()
