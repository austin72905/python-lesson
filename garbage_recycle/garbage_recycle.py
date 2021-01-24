## 垃圾回收

#1. 程序中沒有被引用的對象就是垃圾
#2. 將垃圾對象從內存刪除
#3. python有自動回收機制
#4. 程序結束對象也會被刪除

#### code region ####
class CogMaw:
    def __init__(self):
        self.name ="CogMaw"

    #對象被回收前會被調用
    def __del__(self):
        print("自爆",self)


cogMaw =CogMaw()
cogMaw2 =cogMaw
print(cogMaw.name)

cogMaw =None

input("....")

