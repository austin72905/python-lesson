## 繼承

#1. 繼承可以使類獲得其他類的屬性、方法
#2. 定義類名可以指定父類
#3. 無繼承默認父類是object (所有類都計成是object)
#4. 檢查是否是衍生類 issubclass(類,類)


#### code region ####
class Animal:
    def run(self):
        print("run")

    def sleep(self):
        print("sleep")


class Dog(Animal):
    def bark(self):
        print("dog can bark")

d1 =Dog()
d1.run()