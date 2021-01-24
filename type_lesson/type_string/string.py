##字符串

# 1. 如果字串裡有""(相同的引號不能嵌套)，外面用''
# 2. 長字符串 (如果要打印換行的文字)""" 使用3個引號，會保留字串裡的格式

##轉譯字符

# 1. 使用"\" ，字串裡面有特殊的符號就讓他打印出來，要處理器不要去處理 
# 2. \uxxxx 使用unicode編碼 ex: \u621

##字串格式化

# 1. 合併用"+"，不能與其他類型相加
# 2. print() 可傳2個參數，(像JS)
# 3  %s 任意佔位符 (可指定值)  裡面可傳int、float
# 4. %f 可保留小數
# 5. %d 整數佔位符 (只取整數位)
# 6. 格式化字符串 (在變數前面+ "f")

##字串複製

# 1. 將(字串)與(數值)相乘




#### code region ####

#3  %s 任意佔位符
print("hello %s"%"austin")
print("hello %s 你好 %s"%("austin","tom"))
print("hello %3s"%"ab") #限制最少3個字，少了補空格
print("hello %3.5s"%"ab") #限制最少3~5個字

#4 %f 可保留小數
print("hello %.2f"%123.454) # 保留小數第2位

#6. 格式化字符串
price = 65
product = "魚丸湯"
msg = f"今天喝了{product}，價錢{price}元"
print(msg)

#字串複製
clone = "os"
clone = clone*2
print(clone) #osos

