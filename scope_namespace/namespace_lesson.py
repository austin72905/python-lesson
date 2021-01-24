##命名空間

#1. 指的是變量存儲的位置
#2. 每個作用域都有一個他對應的命名空間
#3. 實際上是一個專名儲存變量的字典dict
#4. locals() 獲取當前作用域的命名空間
#5. locals() 返回的是一個dict，可以透過 命名空間[key]=value 添加變數(不建議)
#6. globals() 獲取全局命名空間


#### code region ####

#5
a=10
nowNameSpace = locals()
print(nowNameSpace)
# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000002088CF33970>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'C:\\Users\\USER\\Python\\python_lesson\\scope_namespace\\namespace_lesson.py', '__cached__': None, 'a': 10, 'nowNameSpace': {...}}

print(nowNameSpace["a"]) # 10