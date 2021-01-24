##數值 : 整數、浮點數

##整數
# 1. 所有整數都是int類型(整數範圍沒有限制)
# 2. 如果數字長度過大，可以用"_" 作為分隔符

##浮點數
# 1. 所有浮點數都是float類型 (盡量不用)
# 2. 對符點數運算可能會得到一個不精確的結果

##其他進制數
# (只要是數字打印，都會是十進制的形式顯示)
# 1. 二進制  0b 開頭
# 2. 八進制  0o 開頭
# 3. 十六進制 0x 開頭



####code region####
float1=0.1
float2=0.2
print(float1+float2)
#0.30000000000000004 與正確答案 0.3 有誤差