# 覆寫

#1. 如果子類跟父類有同方法，創建子類實例時，會調用子類的方法
#2. 會從子類往上找


#### code region ####
class Animal:
    def run(self):
        print("run")

    def sleep(self):
        print("sleep")


class Dog(Animal):
    def bark(self):
        print("dog can bark")

    def run(self):
        print("dog run")


d1 = Dog()
d1.run()