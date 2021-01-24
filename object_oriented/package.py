##封裝 (物件導向三大特性之一)

#1. 隱藏對象中一些不希望外部訪問到的屬性或方法
#1-1. 如何隱藏(封裝)? 設定一個外不不知道的名字 只能使用getter setter 去訪問
#2. getter 獲取對象中的指定屬性  通常都用  get_屬性名(self)
#3. setter 設定對象的指定屬性 set_屬性名(self,要修改的值)
#4. 控制屬性是唯讀 (去掉setter)
#5. __屬性名 or __方法名可以對屬性、方法隱藏，該屬性只能在類的內部訪問 (不推薦)
#6. #5__屬性名 其實是假隱藏，python內部把 __屬性名 =>改成 _類__屬性名
#7. 因為__屬性名沒屁用，所以大部分都用_屬性名表是私有屬性，希望你不要改



#### code region ####


class Dog:
    def __init__(self,name,age):
        #5. __屬性名 可以對屬性隱藏，該屬性只能在類的內部訪問
        self.__hidden_name=name
        self.__hidden_age=age
    #獲取屬性值
    def get_name(self):
        return self.__hidden_name
    #設定屬性值 ，這邊傳入的name 是告數方法要修改成什麼值
    def set_name(self,name):
        self.__hidden_name = name

d1 =Dog("gigi",5)

print(d1.get_name())
#__屬性名，讓外部訪問不到
# d1.hidden_name="hoho" #AttributeError: 'Dog' object has no attribute 'hidden_name'#


#6
d1._Dog__hidden_name="hoho"
print(d1._Dog__hidden_name)
