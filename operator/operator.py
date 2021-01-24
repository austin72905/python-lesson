##算數運算符 +-*/%

# 1. 除法 /
# 2. 除法取整數 //

# 3. 指數乘法 ** (平方根後面就帶0.5)

##賦值運算符 += 、-=

##關係運算符 <、<= 、 is 、 is not

# 1. 字串的比較，實際上是比較unicode編碼(逐位比較)
# 2. is 比較的是id(內存地址)，常對可變對象使用

##邏輯運算符 and、or、not

# 1. not 取相反值 (相當於其他語言的!) ， 非bool值會先轉換成bool，再取反

# 2. result = 1 < 2 < 3 相當於 1<2 and 2<3 (跟中間的數比較)

##三元運算符

# if 條件 else   相當於 isyuan? "a" : "b" (python與其他語言相反)




#### code region ####

##關係運算符
print("2">"1") #True
print("2">"11") #True 逐位比較，首位就比出結果就不往下比了

##三元運算符
isYuan=True
amount =100
money = amount if isYuan else amount*100
print(money)


