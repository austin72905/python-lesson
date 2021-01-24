## 函數在python 是一等公民 (能夠使用函數試編程)

#一等對象特性 (python 裡的對象都是)
#1. 在運行時創建
#2. 能賦值給變量
#3. 能作為參數傳第
#4. 能返回值

#高階函數 (至少有以下一個)   =>實際上是將指定的代碼傳遞進函數
#1. 接收函數作為參數
#2. 能夠將函數作為返回值返回


##閉包  (避免全局變數汙染) 滿神奇的!!
#1. 函數嵌套 (函數內定義函數)
#2. 以內部函數作為返回值返回
#3. 內部函數必須使用到外部函數的變量


#### code region ####
##高階函數
list1 = [1,2,3,4,5]

def count(calfunc,calList:list):
    anser_list= []
    for item in calList:
        #把函數當作參數傳進來
        if calfunc(item):
            anser_list.append(item)
    return anser_list

def isDouble(num):
    if (num%2 ==0):
        return True
    return False

def isSingle(num):
    if(num%2==1):
        return True
    return False

print(type(isDouble))
print(count(isDouble,list1))
    
##閉包
#ex 計算list內元素的總和
#沒有使用閉包的情況，其他人能夠汙染全局變數
test_list=[]
def make_sum(num):
    test_list.append(num)
    return sum(test_list)

print(make_sum(2))
print(make_sum(3))
#test_list.append("2") # 因為插入了一個字串 所以無法計算總合
print(make_sum(4))

print("----使用閉包----")
##使用閉包
def make_sum2():
    #把變數寫在函數裡面
    test_list2=[]
    # 在函數內定義函數
    def cal_sum(nums):
        test_list2.append(nums)
        return sum(test_list2)
    # 將函數作為返回值返回
    return cal_sum

#調用函數
answer = make_sum2()
print("answer 的型別 :",type(answer))
print(answer(1))
print(answer(2))
print(answer(3))
# 一般來說 函數內部的變數(test_list2)，調用完函數就會銷毀，
# 但是因為內部函數要訪問外部函數的變數(test_list2)
# 外部函數的變數不會消失，同時其他人也無法訪問到test_list2 這個變數，避免他被汙染
