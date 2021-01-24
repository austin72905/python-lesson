##函數

#1. 也是對象
#2. 創建函數  def 函數名():
#3. 調用   函數名()


##參數

#1. 可以傳遞的時候 指定哪個參數要什麼值，就不用照位置
#2. 按照位置傳參數跟指定參數時，位置參數要放前面
#3. 可以傳任意類型(func可以傳 又稱"回調函數")
#4. 如果參數是傳list、dic(可變對象)... 函數的修改會改到外面的對象 (除非傳副本，或是使用切片)
#5. 不定長參數  使用*  ，可以把傳入的參數變成list ， *參數之後的參數，要用指定參數傳進去，不然會抓不到
#6. 開頭的參數直接寫 *，則所有參數都要以指定參數傳遞
#7. **參數，只能寫到最後，可以接收其他指定參數，保存到dict

##解包
#8 傳遞參數(tuple、list ...序列)時加* ，他會剛好對應到函數的個數
#9 傳遞參數(dict)時加** ，他會剛好對應到函數的個數

#10. 可以在參數後面加上 :型別，雖然無強制性，但是對於助於代碼理解
#11. 在函數的: 前面加上 ->型別，無強制性，但是對於助於代碼理解 要回傳什麼類型的值

##返回值
#1. return
#2. return 後面的代碼不會執行 


#### code region ####
def funcSpeak(name="tom",age=5):
    print(f"我是{name}，今年{age}歲")

#調用
funcSpeak(age=6,name="austin")

#6 如果傳位置參數 TypeError: funcStarFirst() takes 0 positional arguments but 4 were given

def funcStarFirst(*,a,b,c):
    print("a=",a)
    print("b=",b)
    print("c=",c)

funcStarFirst(a=1,b=2,c=3)

#8傳遞參數(tuple、list ...序列)時加* ，他會剛好對應到函數的個數

def funcDistrucList(a,b,c):
    print("a=",a)
    print("b=",b)
    print("c=",c)

my_tuple=(55,66,77)
funcDistrucList(*my_tuple)

#9 傳遞參數(dict)時加** ，他會剛好對應到函數的個數

def funcDistrucDic (name ,age , sex):
    print("name=",name)
    print("age=",age)
    print("sex=",sex)

my_dic={"name":"austin","age":10,"sex":"男"}

funcDistrucDic(**my_dic)
