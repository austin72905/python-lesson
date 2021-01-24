##標準庫
import sys
import os
import pprint

## pprint

#1. 美化打印結果

## sys =>獲取python解析器的訊息

#1. argv =>獲取命令行的參數
#2. modules => 獲取當前程序引入的所有模塊
#3. path => 模塊的搜索路徑 (搜索模塊的順序)
#4. platform => 平台(win、linux)
#5. exit("msg") =>退出程序

## os => 操作系統

#1. environ(["path"]) =>獲取系統環境變量，可以指定要看哪個
#2. system("命令") =>執行操作系統指令

print(sys)  #<module 'sys' (built-in)>
print(sys.argv)  #['standard_lib.py']
#pprint.pprint(sys.modules)
print(sys.platform)  #win32

print(
    os
)  #<module 'os' from 'C:\\Users\\USER\\AppData\\Local\\Programs\\Python\\Python39\\lib\\os.py'>
