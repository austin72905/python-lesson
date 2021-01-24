## 多重繼承

#1. 可以一個類繼承多個類  類名(父類,父類)
#2. 開發中避免多重繼承

#3. __bases__ 獲取當前類的所有父類 (返回tuple) ，不會找父類的父類
#4. 語法 類名.__bases__


#### code region ####

class A:
    pass

class B(A):
    pass

class C(B):
    pass

print(C.__bases__) #(<class '__main__.B'>,)  