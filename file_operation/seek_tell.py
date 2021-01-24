## seek()、tell()

## 多用於以"二進制形式"讀文本文件

#1. 以這種方式讀，是讀字節 ，最前方會有個b 代表是二進制形式讀取
#2. 讀英文時 python 幫你轉成acsii了
#3. 讀中文時 是unicode 編碼，要自己轉
#4. 如果一般模式讀文本，面對中文時，注意是3個字節 seek() 位置一定要是3的倍數，否則會報錯

## tell()  獲取當前讀到字節的為置

## seek(位置,計算方式)  修改當前讀到字節的為置

#1. 位置 若是"負數"，會從後面開始算，通常會搭配計算方式= 2

#2. 計算方式
#   (1) 0 從頭計算，默認值
#   (2) 1 當前位置
#   (3) 2. 從最後位置

#### code region ####

file_name = "C:/Users/USER/Python/python_lesson/file_operation/poem.txt"
with open(file_name, "rt", encoding="utf-8") as file_obj:
    file_obj.seek(9)
    print(file_obj.tell())
    print(file_obj.read())