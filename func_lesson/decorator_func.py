## 裝飾器

#1. 函數式編程可以把函數使用裝飾器包裝起來，實現對函數的擴展
#2. 可以使用語法糖@ 在要裝飾的函數前 加上@裝飾器函數
#3. 函數可以加上多個裝飾器 ， 先裝飾的會包裝後裝飾的


#### code region ####
# 需求，希望在以下參數執行開始跟結束前都要打印 開始and 結束
def fn1():
    print("我是fn1 函數")

def fn2():
    print("我是fn2 函數")

def add(num1,num2):
    print(num1+num2)


#可以使用高階函數的特性 
#將函數以參數方式傳進去
#外部函數返回一個函數
#裝飾器函數
def decorator_func(callFunc):

    #*參數 接收位置參數  **參數 接收指定參數
    #這個寫法可以涵蓋所有的參數，不傳也OK
    def add_decorator(*posArgs,**keywordArgs):
        print("開始")
        #調用外部傳進來的參數函數
        #這邊的*posArgs,**keywordArgs 是解包的意思，傳給調用的函數
        result = callFunc(*posArgs,**keywordArgs)
        print("結束")
        return result

    return add_decorator

#調用裝飾過的函數
result1 = decorator_func(fn1) #result1 =>是一個函數
print("result1",result1())

result2 = decorator_func(fn2) #result2 =>是一個函數
print("result2",result2())

result3 = decorator_func(add) #result3 =>是一個函數
print("result3",result3(5,6)) #11

#2. 可以使用語法糖@ 在要裝飾的函數前 加上@裝飾器函數
#  有一個減法的函數minor 也想要執行開始跟結束前都要打印 開始and 結束
@decorator_func
def minor(num1,num2):
    return num1-num2

#調用就會是裝飾過的
print("減法",minor(6,9))



#3. 函數可以加上多個裝飾器 ， 先裝飾的會包裝後裝飾的
def decorator_func2(callFunc):

    #*參數 接收位置參數  **參數 接收指定參數
    #這個寫法可以涵蓋所有的參數，不傳也OK
    def add_decorator(*posArgs,**keywordArgs):
        print("兩個開始")
        #調用外部傳進來的參數函數
        #這邊的*posArgs,**keywordArgs 是解包的意思，傳給調用的函數
        result = callFunc(*posArgs,**keywordArgs)
        print("兩個結束")
        return result

    return add_decorator

@decorator_func2
@decorator_func
def sex(num1,num2):
    return num1*num2

print("---------------")
print(sex(5,2))