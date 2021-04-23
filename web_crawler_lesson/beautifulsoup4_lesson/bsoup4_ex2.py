import requests
import bs4

# 從大學排名網將訊息爬取下來

# 定向爬蟲 : 給定url 去爬取，不會擴展到其他url
# 內容不是動態插入html的

#.strip() 去空格

## string 跟 text 差異
# https://zhuanlan.zhihu.com/p/30911642
#.string返回为空，因为文本数>=2，string不知道获取哪一个

#.text返回的是，两段文本的拼接。

url = 'https://www.shanghairanking.cn/rankings/bcur/2020' # 大學排名網 網址

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
soup = bs4.BeautifulSoup(content,'html.parser')

# tbody 是所有大學的訊息 tr 又分別是每一所大學的詳細訊息
#<tbody>
#   <tr>
#       <td>1</td>
#       <td>2</td>
#       <td>3</td>
#   </tr>
#</tbody>
## 上面結構呈現出來的是 1 row 3 col 的 表


def getInfolist(soup):
    infolist=[]
    for trTag in soup.find('tbody').children:       
        #children 會把<></>之間的字串也算進來，所以要過濾掉
        if isinstance(trTag,bs4.element.Tag):
            tdTags =trTag('td')
            # 每一row 的 第一個col 是排名
            #print(tdTags[0].text.strip())
            
            eachInfoList=[]
            # 想要取? col
            for col in range(5):               
                eachInfoList.append(tdTags[col].text.strip())
            #會變成二微陣列
            infolist.append(eachInfoList)  
    # 會是一個二微陣列
    return infolist

infolist = getInfolist(soup)

def printResult(resultList):
    #格式化方法 {} 會對應後面的字串
    #print('{:^10}\t{:^6}\t{:^10}'.format('排名','學校','省分'))

    # chr(12288) 中文format 中間有加空格，預設會用英文空格，導致難以對齊(寬度不一致)，用此方法可改成以中文空格
    #^<> 表示要往哪對齊，數字代表寬度
    template='{0:^10}\t{1:{5}<8}\t{2:^8}\t{3:^8}\t{4:<8}'
    print(template.format('排名','學校','省分','類型','總分',chr(12288)))
    for row in range(len(resultList)):
        eachRow =resultList[row]
        collageName= eachRow[1].split('   ')[0]
        #print('{:^10}\t{:^6}\t{:^10}'.format(eachRow[0],collageName,eachRow[2]))
        print(template.format(eachRow[0],collageName,eachRow[2],eachRow[3],eachRow[4],chr(12288)))
printResult(infolist)


# https://blog.jaycetyle.com/2018/01/python-format-string/

# 第一代版本
# for trTag in soup.find('tbody').children:
#     #children 會把<></>之間的字串也算進來，所以要過濾掉
#     if isinstance(trTag,bs4.element.Tag):
#         tdTags =trTag('td')
#         # 每一row 的 第一個col 是排名
#         print(tdTags[0].text.strip()+","+ tdTags[1].text.strip()+","+tdTags[2].text.strip()+","+tdTags[3].text.strip()+","+tdTags[4].text.strip()) # 顯示排名  .strip() 去空格
    

