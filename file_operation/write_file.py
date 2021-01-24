##寫文件

#1. write(內容)
#2. 可以多次寫入內容
#3. 會返回寫入的文字個數
#4. 使用open 打開文件時，要指定文件要做的操作(預設是讀)
#5. 在 open 設定mode "w" "r" "a" "x"
#   (1) w 是只能寫內容(不會覆蓋) ， #文件不存在會創立文件，文件存在會覆蓋原有內容
#   (2) r 是只能讀內容
#   (3) a 是只能追加內容
#   (4) + 為操作符增加功能 r+ 可讀可寫，文件不存在會報錯  w+ 、  a+ 可讀可寫
#   (5) x 文件不存在就創建，存在就報錯


#### code region ####
file_name ="C:/Users/USER/Python/python_lesson/file_operation/poem.txt"
with open(file_name,"r+",encoding="utf-8") as file_obj:
    count= file_obj.write("低頭吃邊當\n")
    #content = file_obj.read() # 讀不到第一行覆寫的低頭吃邊當
    print(count) #6