## dict 字典

#1. 查詢速度較list 快
#2. key 是唯一 ，重複會替換掉前面的
#3. key 只能是不可變對象(int、str、bool、tuple、None) 
#4. 用{} 創建

## dict()
#5. 將變數傳到函數 dict() 也可以創建  (變數名=>key,值=>value ,type=>str)
#6. 如果序列裡面的"值"，也是序列(子序列)，子序列又只有兩個值，可以用dict()轉換成dic

#7. len()獲取dic 元素個數
#8. in 、not in  字典 裡key 是否存在
#9. 刪除 del dict[key] 

##方法
#10. dic.get(key,"默認值")  獲取值，值不存在返回默認值;沒設默認值返回None 不報錯
#11. dic.setdefault(key,value)  添加kv，如果key存在，不會修改，key不存在就增加kv
#12. dic.update(dic2) 將其他字典的kv 添加到字典中(合併字典) ，重複的會被dic2覆蓋
#13. popitem() 隨機刪除一個kv，返回刪除的kv的tuple ， 刪除空{} 會報錯
#14. pop(key,默認值) 刪除指定的key，返回刪除的value ，如果刪除不存在的，返回默認值，沒設報錯 
#15. clear() 刪除所有kv
#16. copy() 對字典做淺複製(創造副本)，只會簡單複製對象內部的值，如果值也是個"可變對象"，這個可變對象不會被複製

##遍歷
#17. keys() 會返回所有的key 的list
#18. values() 會返回所有的value 的list
#19. items() 會返回kv 的 list ， kv會是tuple 

#### code region ####

#6
list1 = [("name","austin"),("age",18),("sex","男")]
dic1 = dict(list1)
print(dic1) # {'name': 'austin', 'age': 18, 'sex': '男'}

#16

dic2 = {'aa':{'name': 'austin'}, 'age': 18, 'sex': '男'}
dicCopy = dic2.copy()

#淺複製指複製外層，如果值是可變對象，就不會複製
#所以這邊修改值，dic2也會被修改
dicCopy['aa']['name']='mandy'

print(dic2)
print("複製的",dicCopy)