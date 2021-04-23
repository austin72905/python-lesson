import re

## re 庫

# 採用 raw string 類型(不包含轉譯符，不會把\編譯為轉譯符)表 正則表達式 表 r'text'
# 用 一般 string 類型 處理轉譯符 \\ 比較麻煩

## 主要方法
#1. re.search( pattern, string , flags=0) 返回match 對象

#2. re.match( pattern, string , flags=0)  只在起始位置匹配，返回match 對象

#3. re.findall( pattern, string , flags=0) 返回列表，所有符合的字串

#4. re.split( pattern, string , maxsplit=0 , flags=0) 找到符合的元素，把符合結果的部份去掉，返回列表
#   (1) maxsplit : 最大分割數， 超過的部分會在最後一個元素

#5. re.finditer( pattern, string , flags=0) 如果符合的超過一個 ，每個迭代類型返回的是一個match 對象

#6. re.sub( pattern, repl ,string , count=0 ,flags=0) 返回替換後的"字串"
#   (1) repl : 替換匹配的字串
#   (2) count : 最大替換次數

## 參數
# pattern : 正則表達式字串
# string : 檢查是否符合的字串
# flags : 正則表達式的標記
#        (1) re.I  (re.IGNORECASE) 忽略正則表達式大小寫 [A-Z] 能匹配小寫字符
#        (2) re.M  (re.MULTILINE)  正則表達式中 ^ 操作，可以檢查 "每行"的開頭是否符合
#        (3) re.S  (re.DOTALL)     正則表達式中 . 操作，可以匹配所有字符 (原本. 不能匹配\n 換行符)



## 另一種用法 

# pat = re.compile 將正則表達式字串，編譯成對象 (如果都是用同一個正則字串(多次使用)，因為編譯過效率較高)
# 用類型調用方法 pat.search('BIT 100081')  少一個pattern參數

## match 對象

# 屬性
#1. .string : 待檢查的文本
#2. .re : 匹配時用的pattern 對象
#3. .pos : 正則表達式搜索的開始位置
#4. .endpos : 正則表達式搜索的結束位置

# 方法
#1. .group(0) : 獲得匹配後的字串 (只會返回第一個符合的結果，多個要用 finditer)
#2. .start() : 符合的字串在原始字串的開始位置
#3. .end() : 符合的字串在原始字串的結束位置
#4. .span() : 返回元祖(.start(),.end())




#### code region ####

#1. re.search( pattern, string , flags=0) 返回match 對象
# 以中國郵政編碼為例
match = re.search(r'[1-9]\d{5}','BIT 100081')
if match:
    print(match.group(0)) # 100081

#2. re.match( pattern, string , flags=0)  只在起始位置匹配，返回match 對象
match = re.match(r'[1-9]\d{5}','BIT 100081')
if match:
    print(match.group(0)) # 什麼都沒有(match 對象為 null) 

match = re.match(r'[1-9]\d{5}','100081 BIT')
if match:
    print(match.group(0)) # 100081

#3. re.findall( pattern, string , flags=0) 返回列表，所有符合的字串
mlist = re.findall(r'[1-9]\d{5}','BIT100081 TSU100084')
print(mlist) # ['100081', '100084']

#4. re.split( pattern, string , maxsplit=0 , flags=0) 找到符合的元素，把符合結果的部份去掉，返回列表
# maxsplit : 最大分割數， 超過的部分會在最後一個元素
mlist = re.split(r'[1-9]\d{5}','BIT100081 TSU100084')
print(mlist) # ['BIT', ' TSU', '']

mlist = re.split(r'[1-9]\d{5}','BIT100081 TSU100084',maxsplit=1)
print(mlist) # ['BIT', ' TSU100084']

#5. re.finditer( pattern, string , flags=0) 如果符合的超過一個 ，每個迭代類型返回的是一個match 對象
for m in re.finditer(r'[1-9]\d{5}','BIT100081 TSU100084'):
    if m:
        print(m.group(0)) 
        # 100081
        # 100084

#6. re.sub( pattern, repl ,string , count=0 ,flags=0) 返回替換後的字串
matchStr = re.sub(r'[1-9]\d{5}',':FUCK','BIT100081 TSU100084')
print(matchStr) # BIT:FUCK TSU:FUCK


## match 對象
print(type(match)) #<class 're.Match'>
match = re.search(r'[1-9]\d{5}','BIT100081 TSU100084')
if match:
    print(match.group(0)) # 100081 (只會返回第一個符合的結果，多個要用 finditer)
    print(match.string) # BIT100081 TSU100084
    print(match.re) # re.compile('[1-9]\\d{5}')
    print(match.pos) # 0
    print(match.endpos) # 10
    print(match.start()) # 3
    print(match.end()) # 9
    print(match.span()) # (3,9)