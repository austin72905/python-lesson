
#讀文件

#1. 調用open()
#2. 默認以文本文件，默認的encoding = None (默認會以 acsii)
#3. 讀中文文件時 要指定encoding = "utf-8"
#4. 調用 read() 讀取，會一次性讀完

##文件可以分成兩種類型
#1. utf-8 編寫的文本文件
#2. 二進制文件 (圖片、mp3、ppt)

## read()

#1. size 參數 默認 =-1  會一次性讀完所有字符，可以設定一次要讀幾個
#2. 讀完後指針會變，像是json的inputstream
#3. 字符 < size 就讀剩下的
#4. 透過循環來讀整份文件 (##讀取大文件)

## readline() 

#1. 每次讀取一行
#2. 讀完後指針會變，像是json的inputstream
#3. 結束會自帶\n


## readlines()

#1. 一行一行讀取，但她會一次性讀取內容，封裝到list
#2. 讀完後指針會變，像是json的inputstream
#3. 結束會自帶\n


# 對文件物件用 for 循環，也會一行一行讀






#### code region  ####

#讀文件
file_name ="C:/Users/USER/Python/python_lesson/file_operation/poem.txt"
with open(file_name,encoding="utf-8") as file_obj:
    content =file_obj.read()
    print(content)


#4. 透過循環來讀整份文件
file_name ="C:/Users/USER/Python/python_lesson/file_operation/demo.txt"
file_content = ""
with open(file_name) as file_obj:
    
    readSize =20
    while True:
        content = file_obj.read(readSize)

        if (not content):
            break
        #print(content,end="")
        file_content+=content


print(file_content)


