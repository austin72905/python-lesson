## 多態

#1. 非多態:  只是用一種類型的對象，無法處理其他類型對象導致函數通用性非常差


## 鴨子類型
# 如果有東西走路像鴨子，叫聲像鴨子  那他就是鴨子 (只要符合某個特徵，就可以使用函數，不用管他確切的型別)  

#1. ex class 裡面有 __len__ (可以自己定義) 就能使用 len()參數

#### code region ####
class Train:
    def __len__(self):
        return 10
tr = Train()

print(len(tr))