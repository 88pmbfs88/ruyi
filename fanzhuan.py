num = input("请输入一个数字：")
# 数字类型转换
# 得到输入字符串的长度
num_len = len(num)
# 转换为整数
num_int = int(num)
# 取出各个整数
a = int(num)//(10**(num_len-1))     # 1
# b = int(num)//(10**(num_len-2))   # 12
# c = int(num)//(10**(num_len-3))   # 123
shiwei = (num_int - a * (10**(num_len-1)))
b = shiwei//(10**(num_len-2))
c = (shiwei - b * (10**(num_len-2)))//(10**(num_len-3))


bai = 123//100
tmp_shi = 123%100
shi = tmp_shi//10
ge = tmp_shi%10

e = ge *100 + shi * 10 + bai
print(e)



d = c * (10**(num_len-1)) + b * (10**(num_len-2)) + a * (10**(num_len-3))
print(d)


# 字符串类型转换
e = num[2] + num[1] + num[0]
f = num[-1] + num[-2] + num[-3]
print(f)
print(e)

# aa,bb,cc = input("请输入：")
# dd = cc * (bb - aa - 1)
# print(dd)

# 1，4，3
dd = 1 + (3-1) * (4 - 1)
print(dd)
