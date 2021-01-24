## 異常

#1. 一旦出現異常成續會立即中止
#2. 語句 try:  可能出錯的代碼   except: 出現錯誤的處理語句 ... else 沒有出錯時執行的語句 
#3. 通過異常處理，避免程序中止
#4. 異常訊息都會保存到一個專門的異常對象中 (報錯時 駝峰式的類TypeError...)
#5. finally => 不論是否出現異常，該子句都會執行


#### code region ####

try:
    #可能出錯的代碼
    print(10/0)
except:
    #出現錯誤的處理語句
    print("some error occur")

else:
    #沒有出錯時執行的語句
    print("success")
finally:
    print("done")
