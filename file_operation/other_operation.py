import os
from pprint import pprint
# pprint 美化的打印
#這樣就不用.了
#引入os 包

get_menu_list = os.listdir()  # 獲取指定目錄結構 (默認當前 參數 path=".")

get_now_menu = os.getcwd()  # 獲取當前目錄

chg_menu = os.chdir()  # 切換當前目錄  cd

create_menu = os.mkdir()  # 創建目錄  (目錄名)

rm_menu = os.rmdir()  # 刪除目錄

rm_file = os.remove()  # 刪除文件 (文件名)

os.rename() # 改名 ("oldname","newname") 可以在newname 指定新路徑

pprint(get_menu_list)

