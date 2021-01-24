##循環語句

#while、break、continue


# 1. while 條件表達式:
#    執行語句

# 2. pass 佔位符
#    因為python 執行語句一定要寫東西，如果還沒想到要寫什麼可以用pass 暫時代替

#### code region ####

import time

count = 0
#計算整個程式花多少時間
begin = time.time()
while (count<5):
    print(f"目前執行第{count}次")
    #每次打印前休息1秒
    time.sleep(1)
    
    count+=1
end =  time.time()
print(f"總耗時{end-begin}秒")
input("執行結束，按任意見結束..")