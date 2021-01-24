## 魔術方法(特殊方法)
#class 屬性不希望所有對象都能訪問

#1. 特殊方法不需要我們自己去調用
#2. def__魔術方法__
#3. 了解其什麼時候作用
#4. 創建一個實例系統會自己調用

##創建對象的流程
#1. 創建一個變量
#2. 在內存建立一個新對象
#3. __init__(self) 執行
#4. 將對象的id 值給變量

## __init__  (創建一個實例系統會自己調用)

## __str__ (嘗試將對像轉字串時會調用)(當我們打印對象時，是這個特殊方法的返回值)  <__main__.Person object at 0x000001F1DEC47FD0>

## __repr__ (對當前對象使用repr() 函數時調用)  指定對象在 "交互模式" 中直接輸出的效果 (在交互模式直接打實例名，會打印的東西)

## __ lt__(self , other) (<)(當調用比較運算符時調用) self : 當前對象， other : 比較的對象 ， 可以自訂比較規則

## le (<=) 、 eq(==)、 ne(!=)、gt(>)、ge(>=)

## __bool__(self)  轉為true 的條件


#### code region ####

class Person:
    #self 是系統(解析器)預設都會傳的(跟其他語言的this很像)
    #可以自定義要傳進來的參數 (從第二個開始)
    #__init__ 可以用來初始化屬性
    def __init__(self,name="austin"):
        #添加屬性
        self.name =name
        print(f"person建立了 {name}")

    def __str__(self):
        return f"Person [name = {self.name}]"

    def __repr__(self):
        return "hello"

    #回收前會調用
    def __del__(self):
        print("回收",self)
    
    def sayHi(self):
        print(f"你好{self.name}")

p1 =Person()
p1.sayHi()

#可以傳name 參數進去
p2 = Person("王剛")
p2.sayHi()
print(repr(p2))