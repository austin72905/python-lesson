## tuple

# 1. 把它當作不可變的list就行了
# 2. 當希望數據步改變，就使用tuple
# 3. 只要是改變元素值的方法都不能用
# 4. 是一種不可變的序列
# 5. 創建tuple 使用()
# 6. 如果不是空tuple ()可省略，裡面只有一個元素，要加逗號

##解包
# 7. 可以有類似js 解構賦值的方法 a,b = my_tuple
# 8. 變數必須跟 tuple 裡面的元素量相同
# 9. 在變數加* 會把剩餘值存成list (只能有一個*) 可以用在傳遞參數時
# 10. 可以交換值 a,b = b,a


#### code region  ####
##解包
my_tuple = 1,2,3,4,5

first , second , *last = my_tuple

print(first,second,last)
#交換值
first , second = second ,first

print(first,second,last)