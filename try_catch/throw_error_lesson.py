## 拋出異常

#1. raise Exception("msg")
#2. 可以拋出異常，後面加個異常對象
#3. 讓調用者知道函數調用時出問題，讓調用者自己判斷
#   ，有些情況不應該是函數自己判斷 (ex add 函數處理兩正數相加，調用者傳負數近來
#   ，負數本來就不應該出現在這個函數，所以拋出異常要調用者自己處理)
#4. 可以自定義類 繼承 Exception 這個raise 可以自定義類


####  code region  ####
# 如果a、b有負數拋出異常
def add(a,b):
    if a<0 or b<0:
        raise Exception("只可以是正數")

    return a+b

#try:
#    print(add(1,-5))
#except Exception as ex:
#    print(f"Exception occur  {ex}")


print(add(1,-5))

# 這個raise 就可以調用自己定義的類
class ErrClass(Exception):
    pass
