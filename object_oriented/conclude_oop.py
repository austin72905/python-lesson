#定義一個類
class A(object):

    #類屬性
    #1. 直接在類中定義的屬性，可以通過類、實例訪問到
    #2. 無法通過實例來修改
    #3. 只能透過類對象修改
    # (較少使用)
    count = 0

    def __init__(self):
        #實例屬性
        #只能通過實例對象來訪問與修改，不能通過類
        self.name = "ao"

    #實例方法
    #1. 以self 為第一個參數的都是實例方法
    #2. 實例方法在調用時，python 會將調用對象作為self 傳入
    #3. 實例方法可以通過實例、類去調用
    #   (1)實例調用 : 會自動將當前調用對象作為self 傳入
    #   (2)類調用  : 要自己手動傳第self
    def test(self):
        print("這是實例方法",self)

    #類方法
    #1. @classmethod 修飾
    #2. 第一個參數是cls，會被自動傳第，cls就是當前的類對象
    #3. 可以通過實例、類去調用，沒有區別
    #4. 除了第一個參數self、cls 有差異，其他沒有區別
    @classmethod
    def testClaMethod(cls):
        print("這是一個類方法",cls)

    #靜態方法
    #1. #staticmethod 修飾
    #2. 不需要指定參數
    #3. 可以通過類、實例去調用
    #4. 只是個放在class 的函數， 跟class 本身沒什麼關係
    #5. 一般都是依些工具方法，與當前類無關
    @staticmethod
    def static_test():
        print("這是一個靜態方法")



#### test ####

#類屬性
aInstance =A()
print(aInstance.count)
print(A.count)

#實例屬性
print(aInstance.name)
#print(A.name) #type object 'A' has no attribute 'name'

#實例方法
aInstance.test()
#A.test() #TypeError: test() missing 1 required positional argument: 'self'
A.test(aInstance)

#類方法
A.testClaMethod()
aInstance.testClaMethod()

#靜態方法
A.static_test()
aInstance.static_test()