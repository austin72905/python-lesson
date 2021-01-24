## 模塊化

#1. 將成序分別寫到多個文件
#2. 增加可復用性
#3. 一個py文件 就是一個模塊

#4. 引入外部模塊 
#   (1)import 文件名
#   (2)import 文件名 as 別名
#   (3)from 文件名 import 變量,方法
#   (4)from 文件名 import *   (不太建議使用，很容易重複名，又很臃腫)
#   (5)from 文件名 import 變量,方法 as 別名
#5. 模塊的實例只會創建一次
#6. 添加了_ 的變數、方法只能在原本的文件訪問
#7. 有些文件會有測試代碼，但在被其他人引用時，不希望被執行， 
#   可以 if __name__ == "__main__": 來判斷      => (被引用時就不執行以下代碼)

#6. __name__ 可以獲取文件名 ， 在自己文件調用會獲取__main__ 為值，代表為主模塊
#7. 主模塊就是直接通過python 執行的模塊