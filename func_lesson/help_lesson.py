##文檔字符串(doc str)

#1. 用於help(函數) 時，可以顯示出註解

def func1(a:int,b,c):
    '''
    這是文檔字符串，會被打印出來
    '''
    return(a+b+c)

#打印出文檔字符串
help(func1)