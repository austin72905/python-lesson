## super

#1. 子類會繼承父類的所有方法，包含特殊方法
#2. 子類的特殊方法也可以override
#3. 有時候子類只想要父類的其中幾個屬性，用#2 的寫法，要將父類所有的參數複製一遍
#   (又要在子類寫一堆 self._name = name....)，很麻煩
#4. 調用父類的__init 添加參數   語法: 父類.__init__(self,參數)


## super()
#5. #4寫法耦合度太高(直些調Animal) ，可以通過 super() 動態獲取父類， 降低耦合
#6. 語法: super().__init__(參數)     =>不用傳self 


#### code region ####
class Animal:
    def __init__(self,name):
        self._name = name

    def run(self):
        print("run")

    def sleep(self):
        print("sleep")

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        self._name = name


class Dog(Animal):
    def __init__(self,name,age):
        self._name = name
        self._age = age

    def bark(self):
        print("dog can bark")

    def run(self):
        print("dog run")
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,age):
        self._age = age


d1 = Dog("wiwi",5)
print(d1.name)
print(d1.age)
d1.run()

#3 #4

class Cat(Animal):
    def __init__(self,name,age):
        #希望調用父類的__init__，初始化父類中定義的屬性
        Animal.__init__(self,name)
        self._age = age
    

c1 = Cat("mia",3)

print(c1.name)

#5 #6
#super()
class Tiger(Animal):
    def __init__(self,name,age):
        super().__init__(name)
        self._age =age
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,age):
        self._age = age

t1 =Tiger("tiger",12)
print(t1.name)
