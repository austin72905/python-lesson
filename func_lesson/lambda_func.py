##匿名函數

#1. func 作為參數傳遞，有時候只傳一次，可以使用匿名函數
#2. 語法:lambda 參數列表: 返回值

##filter、map
#1. filter 是內建 的一個函數，會返回一個filter object
#2. map 是內建 的一個函數，會返回一個map object

##sort、sorted

# 1. sort() 排序(僅能用在list) 但其實可以傳個(key=函數) 的參數進去 (可以將list中每個元素做類型轉換)
# 2. sorted() 只要是"序列"都能使用，是返回新對象，不會影響原本的

#### code region ####

#2
lambda a, b: a + b  # 參數a,b  return(a+b)的意思

#立即呼叫
#(很象js 立即呼叫函數)
print((lambda a, b: a - b)(7, 3))  #4

#filter 是內建 的一個函數，會返回一個filter object
list1 = [1, 2, 3, 4, 5]


def isDouble(num):
    return num % 2 == 0


answer = filter(isDouble, list1)  #[2, 4]
print(list(answer))
#跟上面一樣效果
answer1 = filter(lambda num: num % 2 == 0, list1)  #[2, 4]
print(list(answer1))

#2. map 是內建 的一個函數，會返回一個map object
# ex: 想把一個列表裡所有的元素+1
answer2 = map(lambda item: item + 1, list1)
print(list(answer2))

##sort、sorted
listSort = ["aa", "ccc", "b", "dddd"]
listSort.sort()  # 默認用unicode 編碼排序
print(listSort)  # ['aa', 'b', 'ccc', 'dddd']

listSort2 = ["aa", "ccc", "b", "dddd"]
listSort2.sort(key=len)  # 以每個元素的長度排序
print(listSort2)  # ['b', 'aa', 'ccc', 'dddd']

listSort3 = [1, "3", "2", "4", 5]  # 應該是無法排序
listSort3.sort(key=int)  # 把每個元素都轉程int 類型
print(listSort3)  # [1, '2', '3', '4', 5]

# 2 sorted 只要是序列都可用
testStr = "21354"
strSort = sorted(testStr, key=int)
print(strSort)  # ['1', '2', '3', '4', '5']
