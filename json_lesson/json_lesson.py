import json
from pprint import pprint

##Json

# 1. 反序列化 json.loads
# 2. 序列化  json.dumps

#### code region  ####
my_dic = dict(name='BOb', age=20, score=93)

json_str = json.dumps(my_dic)
pprint(json_str)  # '{"name": "BOb", "age": 20, "score": 93}'

json_dic = json.loads(json_str)

pprint(json_dic)  # {'age': 20, 'name': 'BOb', 'score': 93}


class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


# dic 轉 class
def dicToClass(dic: dict, className):
    # 對應參數解包丟進去
    return className(**dic)


#what =dicToClass(json_dic,Student)
#print(what._name)


def dicToClass2(dic):
    return Student(**dic)

# dic 轉 class
stud1 = dicToClass(json_dic, Student)

# class 序列化成字串
stud_json_str = json.dumps(
    stud1,
    default=lambda obj: obj.__dict__)  #{"name": "BOb", "age": 20, "score": 93}

print(stud_json_str)

# 字串反序列化成class
#但是class 要寫死不太好
json_str_tostud = json.loads(stud_json_str, object_hook=dicToClass2)
print(json_str_tostud)

# 不用寫死
# 先轉成dic
# 再從dic 轉 class
jstr_dic = json.loads(stud_json_str)
jstr_stud = dicToClass(jstr_dic,Student)
print(jstr_stud)
