## 列表 list

# 1. 保存多個"有序"的數據
# 2. 使用[] 創建，裡面元素可以存任意類型
# 3. 獲取長度 len(列表)
# 4. 索引是負數，會從後面取
# 5. 合併列表 + ， * 會複製列表然後合併
# 6. in 和 not in 檢查元素是否在列表(return bool)
# 7. min() 和 max() 獲取最小/大值
# 7-1. 刪除元素 del 、 修改元素 list[index]=xxx

## 以下為method   ...list.func()
# 8. index(元素) 獲取index ，如果元素不存在會報錯
# 9. count(元素)  獲取元素的數量
# 10. append() 添加元素到最後
# 11. insert(index,元素) 指定位置插入元素
# 12. extend(序列) 將該序列元素的添加到列表
# 13. clear() 清空列表
# 14. pop(index) 刪除index的元素，會返回刪除的元素 (不傳index 默認刪除最後一個)
# 15. remove(元素) 刪除指定元素 
# 16. reverse() 反轉列表
# 17. sort() 排序列表  、 sort(reverse=True) 降序
# 18. 遍歷 for 變數 in 列表:   很像foreach
# 19. range() 可以生成一個自然數序列 
#    (1)起始位置 (默認0)(可省略)
#    (2)結束位置
#    (3)步長 (默認1)


## 切片 (列表的局部)
# 1. 列表[起始:結束(不包含):步長] ， 返回一個新列表，不影響原本的list
# 2. 省略起始:從第一個開始取
# 3. 省略結束:取到最後一個
# 4. 都省略就是全取
# 5. 步長: 是否跳著取(預設1)，如果寫-1 會把整個列表倒序

##序列 (sequence)

# 1. python 裡面的一種數據結構
# 2. 可變序列 (list) (序列中元素是否可改變)
# 3. 不可變 (str、tuple)   => 可以用list(不可變)轉換成列表

##解包
# 4. 只要是序列(list、str、tuple) 都能夠解包
# 5. 可以有類似js 解構賦值的方法 a,b = my_tuple
# 6. 變數必須跟 tuple 裡面的元素量相同
# 7. 在變數加* 會把剩餘值存成list (只能有一個*)
# 8. 可以交換值 a,b = b,a


#### code region ####

#列表
# 7-1. 刪除元素 del 、 修改元素 list[index]=xxx
stus =["austin","julia","mandy","tom","jack"]
print(stus) #['austin', 'julia', 'mandy', 'tom', 'jack']
del stus[0] # 刪除元素
print(stus) #['julia', 'mandy', 'tom', 'jack']

#透過切片修改  ##後面只能傳"序列"來做修改
stus[0:2]="abc" #['a', 'b', 'c', 'tom', 'jack']
print(stus)

#透過切片刪除
del stus[0:2]
print(stus)

# 18. 遍歷 for 變數 in 列表:   很像foreach
for item in stus:
    print(item)

# 19. range(數字) 可以生成一個序列 
r = range(5)
r1 = range(1,5)
r2 = range(1,5,2)
print(r) #range(0, 5)
print(list(r)) #[0, 1, 2, 3, 4]
print(r1) #range(1, 5)
print(list(r1)) #[1, 2, 3, 4]
print(r2) #range(1, 5, 2)
print(list(r2)) #[1, 3]


