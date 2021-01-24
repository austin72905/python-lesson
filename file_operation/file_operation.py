##文件(file)

#1. I/O (Input/Output)
#2. 操作文件的步驟
#   (1) 打開文件
#   (2) 對文件的操作( 讀、寫 )，然後保存
#   (3) 關閉文件


##打開文件

#1. 語法 open(file)
#2. 參數 file : 路徑
#3. 返回值: 打開的文件(obj)
#4. 路徑用/ 取代\ ，或是 \\


## 讀取文件內容

#1. 語法 文件物件.read()
#2. 可將內容存成一個str


##關閉文件

#1. 語法 文件物件.close()
#2. 如果代碼執行完，文件會自動關閉，會自己是放掉資源，但如果下面還有代瑪，還是要自己關掉


##自動關閉

#1. with open(檔案路徑) as 文件物件:
#2. 對文件的操作只能在with 裡面，(會自動關閉)



#### code region ####

##打開文件
file_name="C:/Users/USER/Python/python_lesson/file_operation/demo.txt"
file_obj = open(file_name)
print(file_obj) #<_io.TextIOWrapper name='C:/Users/USER/Python/python_lesson/file_operation/demo.txt' mode='r' encoding='cp950'>

## 讀取文件內容
content = file_obj.read()

print(content)

##關閉文件
file_obj.close()

##自動關閉
#打該文件應該會報錯 FileNotFoundError: [Errno 2] No such file or directory: 'hello'

#試著捕獲錯誤
file_name1="hello"

try:
    with open(file_name1) as file_obj1:
        print(file_obj1.read())
except FileNotFoundError:
    print(f"{file_name1}不存在~~")