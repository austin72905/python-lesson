import re

## 貪婪匹配 (re 庫默認)
# 會輸出匹配"最長"的字串


# 下面的例子符合多項匹配(PYAN、PYANBN...)
match = re.search(r'PY.*N','PYANBNCNDN')
print(match.group(0)) # PYANBNCNDN

# 最小匹配 (加上?)
# 輸出最短的字串
match = re.search(r'PY.*?N','PYANBNCNDN')
print(match.group(0)) # PYAN


## 常用搭配
# *?
# +?
# ??
# (m,n)?