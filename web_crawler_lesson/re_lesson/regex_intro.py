## 正則表達式
#  regular expression
#  用來表達一組字符串特徵的表達式


# ex1
# 假設想要篩選符合下列條件之一的字串
# 'PN'
# 'PYN'
# 'PYTN'
# 'PYTHN'
# 'PYTHON'

# 用正則表達式
# P(Y|YT|YTH|YTHO)?N

# ex2
# 無窮字串祖

# 'PY'
# 'PYY'
# 'PYYY'
# 'PYYYY'
# 'PYYYYY...'

# 用正則表達式
# PY+

# ex3
# 'PY' 開頭，但是長度不超過10，之後的字符不能有'P'、'Y'
# 很難一一列出來
# 'PYABC'  O
# 'PYKXYZ' X => 後續出現Y

# 用正則表達式
# PY[^PY]{0,10}

## 作用
# 表達文本特徵(病毒、入侵)
# 查找或替換一組字串
# 匹配字串的全部或部分

## 正則表達式 語法
#  .        表任何單個字符
# []        字符集，給出取值範圍  [abc] 表a、b、c ; [a-z] 表a~z
# [^]       排除範圍  [^abc] 表非a、非b、非c
#  *        前一個字符無限擴展(含0次)  abc* 表 ab、abc、abcc、abccc
#  +        前一個字符無限擴展  abc+ 表 abc、abcc、abccc
#  ?        前一個字符0 or 1 次擴展  abc? 表 ab、abc
#  |        左右表達式任取其一  abc|def 表 abc、def
# {m}       擴展前一個字符m次 ab{2}c 表abbc
# {m,n}     擴展前一個字符m~n次 ab{1,2}c 表 abc、abbc
# {m:n}     同上
#  ^        匹配字串開頭 ^abc 表abc且在字串開頭
#  $        匹配字串結尾
#  ()       分組標記 在內部只能使用| (abc) 表 abc、 (abc|def) 表 abc、def
#  \d       數字 等價 [0-9]
#  \w       單詞字符 等價 [A-Za-z0-9_]


# 常用
# ^[A-Za-z]+$             表 由26字母組成的字串
# ^-?\+$                  表整數的 字串
# ^[0-9]*[1-9][0-9]*$     表正整數的 字串
# [\u4e00-\u9fa5]         表中文字串


