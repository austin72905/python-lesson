import requests
import bs4
import pandas as pd

# 說明
# 1. 主要執行方法 是 main() => 去調用 excuteCrawler() => excuteCrawler 裡面在去調用其他方法
# 2. printResult 只是打印，可以不用理他
# 3. 我是用 bs4 解析 html element ， selenium 套件應該也是有相同功能，可以去查查


# 爬取網頁內容
def getHTMLText(url: str, headers: dict) -> str:
    try:
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
        resp.encoding = resp.apparent_encoding
        return resp.text
    except:
        print("url: " + url)
        print("request: " + resp.request)
        print("響應: " + resp.status_code)
        return "error resp"


# 解析內容
def parseContent(content: str) -> list:
    # bs4 套件裡的方法，用這個方法解析出的soup 物件，可以分析html的標籤文字(tag)
    soup = bs4.BeautifulSoup(content, 'html.parser')
    # 裝每支股票排名資料 的list
    infoL = []
    ptr = -1
    # 每支股票都以 {'name':val,'成交價':val,'漲跌':val,'買進張數':val,賣出張數:val...}
    # 的形式存放

    # 最終效果
    # list 裡面裝dict
    # [
    #   {'name':val,'成交價':val,'漲跌':val,'買進張數':val,賣出張數:val...},
    #   {'name':val,'成交價':val,'漲跌':val,'買進張數':val,賣出張數:val...},
    #   {'name':val,'成交價':val,'漲跌':val,'買進張數':val,賣出張數:val...},
    # ]

    # 想要擷取值的tag，該tag 擁有的屬性
    # 可以去瀏覽器 按 f12 看element
    nameTag = ['Lh(20px)', 'Fw(600)', 'Fz(16px)', 'Ell']
    nameTag2 = ['Lh(20px)', 'Fw(600)', 'Fz(14px)', 'Ell']
    priceTag = [
        'Fxg(1)', 'Fxs(1)', 'Fxb(0%)', 'Ta(end)', 'Mend($m-table-cell-space)',
        'Mend(0):lc', 'Miw(72px)'
    ]
    dealCountTag = [
        'Fxg(1)', 'Fxs(1)', 'Fxb(0%)', 'Ta(end)', 'Mend($m-table-cell-space)',
        'Mend(0):lc', 'Miw(78px)'
    ]
    haveCountTag = [
        'Fxg(1)', 'Fxs(1)', 'Fxb(0%)', 'Ta(end)', 'Mend($m-table-cell-space)',
        'Mend(0):lc', 'Miw(98px)'
    ]
    stockNumTag = ['D(f)', 'Ai(c)']
    # 找到有 M(0) P(0) List(n) 這個屬性 且是 ul 的 tag
    # 遍歷他裡面所有的子孫節點
    for tag in soup.find('ul', 'M(0) P(0) List(n)').descendants:
        # 子孫節點 連 tag 包住的 文字部分也會搜尋到，要過濾掉
        if isinstance(tag, bs4.element.Tag):
            # tag 屬姓
            attrsVals = tag.attrs.values()
            # 股票名 所在的tag 屬性可能是 nameTag 或 nameTag2
            # 所以只要找到這兩個屬性，代表找到股票名了
            if (nameTag in attrsVals):
                ptr += 1
                # 取得 tag 夾住的值 ex: <div>會得到這裡的值</div>
                name = tag.text
                infoL.append({'name': name})

            elif (nameTag2 in attrsVals):
                ptr += 1
                name = tag.text
                infoL.append({'name': name})
            elif (stockNumTag in attrsVals):
                sn = tag.text
                infoL[ptr].setdefault('股號', sn)
            elif priceTag in attrsVals:
                price = tag.text

                if '成交價' not in infoL[ptr].keys():
                    infoL[ptr].setdefault('成交價', price)
                else:
                    infoL[ptr].setdefault('漲跌', price)

            elif dealCountTag in attrsVals:
                num = tag.text

                if '買進張數' not in infoL[ptr].keys():

                    infoL[ptr].setdefault('買進張數', num)

                elif '賣出張數' not in infoL[ptr].keys():

                    infoL[ptr].setdefault('賣出張數', num)

                elif '賣超張數' not in infoL[ptr].keys():

                    infoL[ptr].setdefault('賣超張數', num)

                elif '成交張數' not in infoL[ptr].keys():

                    infoL[ptr].setdefault('成交張數', num)

            elif haveCountTag in attrsVals:
                num = tag.text

                if '持股張數' not in infoL[ptr].keys():

                    infoL[ptr].setdefault('持股張數', num)

                elif '持股比率' not in infoL[ptr].keys():

                    infoL[ptr].setdefault('持股比率', num)

    return infoL


def printResult(slist):
    template = '{0:<8}\t{1:^6}\t{2:>5}\t{3:>8}\t{4:^8}\t{5:^8}\t{6:>8}\t{7:>8}\t{8:>8}\t{9:>8}'
    print(
        template.format("name", "成交價", "漲跌", "買進張數", "賣出張數", "賣超張數", "成交張數",
                        "持股張數", "持股比率"))
    for info in slist:
        print(
            template.format(info['name'], info['成交價'], info['漲跌'],
                            info['買進張數'], info['賣出張數'], info['賣超張數'],
                            info['成交張數'], info['持股張數'], info['持股比率']))


def excuteCrawler(url: str, headers: dict):

    # 爬取網頁內容
    content = getHTMLText(url, headers)
    # 解析
    slist = parseContent(content)

    # 將slist 理資料 轉成 pandas 可以接收的格式
    arr = []
    for item in slist:
        arr.append(item.values())

    # columns 指定欄位名稱
    df = pd.DataFrame(arr, columns=slist[0].keys())
    # 看要打印多少rows 出來
    print(df[0:50])
    print()


def main():

    baseUrl = "https://tw.stock.yahoo.com"
    # 個排行的api
    urlDict = {
        "外資賣超排行": "/rank/foreign-investor-sell",
        "自營商買超排行": "/rank/dealer-buy",
        "自營商賣超排行": "/rank/dealer-sell",
        "投信買超排行": "/rank/investment-trust-buy",
        "投信買賣超排行": "/rank/investment-trust-sell"
    }

    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }

    # 執行個排行的爬取
    for rankname in urlDict.keys():
        print(rankname)
        print()
        # 如 https://tw.stock.yahoo.com/rank/foreign-investor-sell
        excuteCrawler(baseUrl + urlDict[rankname], headers)


# 主要執行 main 方法 ， main 方法裡面才去調用其他方法
main()
