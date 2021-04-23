import requests
import os

## 抓取圖片

url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Stary_pies.jpg/800px-Stary_pies.jpg'

target ='C:\\Users\\USER\\Python\\python_lesson\\web_crawler_lesson\\dog.jpg'

if os.path.exists(target):
    print("圖片已存在")
    os._exit(0) #0 無錯誤退出

def getHTMLText(url:str):
    try:
        headers = {'User-Agent':'Mozilla/5.0'}
        resp = requests.get(url,headers=headers,timeout=30)
        print(resp.request.headers)
        resp.raise_for_status()
        #resp.encoding = resp.apparent_encoding
        
        return resp.content
    except:
        return "爬取異常"

picContent = getHTMLText(url)

#print(picContent)

#wb 寫 二進制文件
with open(target,'wb') as file_obj:
    file_obj.write(picContent)
    file_obj.close()
    print("圖片保存成功")
