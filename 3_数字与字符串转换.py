"""
定义一个年份数字 （整形）
定义一个长度（浮点型）
定义一个长度（字符串类型）

"""
# 标识符 赋值符 值
nianfen = 2021
changd = 11.2
changdu = "11"

"""
依次把三个变量转化为其他两种类型
"""
# type()

# nianfen
# int > str :

A = str(nianfen)
print("int > str ：%s " % type(A))

a = float(nianfen)
print("int > float : %s " % type(a))

# chagd
b = str(changd)
print("float  > str : %s " % type(b))

c = int(changd)
print("float > int : %s " % type(c))

# changdu
d = float(changdu)
print("str > float : %s " % type(d))
e = int(changdu)
print("str > int : %s " % type(e))
