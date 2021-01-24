##裝飾器@property

#1. 裝飾器@property  getter 方法 可以不用加()就能訪問(像調用屬性一樣)
#2. 使用property 的方法必須和屬性名一樣
#3. setter 裝飾器 @屬性名.setter
#4. property裝飾器一定要有getter

#### code region ####
class Person:
    def __init__(self,name):
        # 因為__屬性名沒屁用，所以大部分都用_屬性名表是私有屬性，希望你不要改
        self._name = name

    #加上裝飾器@property 的getter
    #調用時可以不用加() ，像是調用屬性一樣
    @property
    def name(self):
        return self._name
    
    #加上裝飾器@property 的setter
    @name.setter
    def name(self,name):
        self._name=name

p1 =Person("audtin")
#調用方法
print(p1.name) #audtin
#調用setter 方法
p1.name="wan"
print(p1.name)