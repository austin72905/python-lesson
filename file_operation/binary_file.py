##二進制文件

#1. 開啟圖片、mp3
#2. 調整open( mode 參數)
#3. 一般文本文件 mode t (默認值可不寫) "w" 其實是=> "wt"
#4. 二進制文件 修改為 b 改成 => "wb" 、 "rb"
#5. 讀取文本文件是以字符為單位
#6. 讀取二進制文件是以字節為單位



####  code region  ####

# 需求: 將圖片複製到target 資料夾
#圖片 (二進制文件)
file_name = "C:/Users/USER/Python/python_lesson/file_operation/woman2.png"
target_name = "C:/Users/USER/Python/python_lesson/file_operation/target/womancopy.png"
with open(file_name,"rb") as file_obj:
    
    with open(target_name , "wb") as target_obj:
        #1024字節=1k
        #一次讀100k
        chunk =1024 * 100

        while True:
            #讀數據
            content = file_obj.read(chunk)

            if (not content):
                break
            target_obj.write(content)
