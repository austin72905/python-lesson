##面相對象
#關注的是對象

##面向過程
#將功能拆解為一個一個步驟，通過完成一個一個步驟來完成程序
#但這種代碼往往只是用一個功能，可複用性較低


#ex 孩子上學
# 面向過程 (只能實現一個功能)

#1. 媽媽起床
#2. 媽媽上廁所
#3. 媽媽刷牙
#4. 媽媽做早飯
#5. 媽媽叫孩子起床
#6. 孩子上廁所
#7. 孩子刷牙
#8. 孩子吃早飯
#9. 孩子去上學

#面相對象

#1. 孩子他媽起床叫孩子去上學 (真正的細節在對象內部裡面，還是要寫步驟，只是寫到對象裡了)

#類(class)

#1. 對象的藍圖 ，對象則是class 實例
#2. 定義類開頭要大寫
#3. class 類名([父類]):        ...([父類])可略
#4. 創建對象  變量=類名()
#5. isinstance(對象,類) 檢查一個對象是否是一個類的實例
#6. class 本身也是type類型的對象
#7. 能夠為class添加屬性
#8. 也可以在class 定義共有屬性
#9. class 裡面定義的函數稱為 方法 (一定要設置一個參數)，但不一定要傳
#10. #9是因為方法沒辦法直接訪問屬性
#11. #9 方法設定的第一個參數，會傳調用方法的對象本身，一般都會定義成self (像是js 的 this)


#### code region ####

#2

class Myclass():
    pass

print(Myclass) # <class '__main__.Myclass'>
#4. 創建實例
c1 =Myclass()
print(c1)  # <__main__.Myclass object at 0x00000136F87F4FD0>

#5. 
print(isinstance(c1,Myclass)) # True

#7. 能夠為class添加屬性
class Myclass2:
    pass


c2 =Myclass2()
#添加屬性
c2.name="austin"
print(c2.name)

#8. 也可以在class 定義共有屬性
#9. class 裡面定義的函數稱為 方法 (一定要設置一個參數)，但不一定要傳
class Myclass3:
    name="悟空"
    #方法沒辦法直接訪問屬性
    def sayHi(lan):
        print("早安")

c3 = Myclass3()
print(c3.name)
#調用方法
c3.sayHi()

#10. #9是因為方法沒辦法直接訪問屬性
#11. #9 方法設定的第一個參數，會傳調用方法的對象本身，一般都會定義成self (像是js 的 this)
class Myclass4:
    name:""
    def SayHello(self):
        print(f"第一個參數是{self}")
        print(f"你好{self.name}")

c4 =Myclass4()
c4.name="austin"
#調用方法
c4.SayHello()
