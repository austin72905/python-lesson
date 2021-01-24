## 異常對象

#1. Exception 是所有異常對象的父類
#2. 只寫一個except， 跟 except Exception 是一樣的，代表捕獲所有異常
#3. 可以各自類別捕獲到各種異常時，要做出對應的動作 (多個except)
#4. 可以把 異常對象 as 變量， 可以看到錯誤的內容


try:
    l[10]
    print(10/0)

except NameError as nr:
    print(f"NameError occur msg : {nr}")
except ZeroDivisionError as zr:
    print(f"ZeroDivisionError occur msg : {zr}")

except Exception as ex:
    print(f"Exception occur msg : {ex}")
finally:
    print("done")
