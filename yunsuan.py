"""
周长： PI * R * 2
面积： PI * R ** 2
"""

# r = input("大哥请输入半径：")
# PI = 3.14
# print("周长是：%s"%(PI * float(r) * 2))
# print("面积是：%s"%(PI * float(r) ** 2))


"""
三个数求出最大值、最小值
"""
# a, b, c = 5, 1, 3


"""
求出商和余数
"""
# a = int(input("A = ："))
# b = int(input("B = ："))
# print("商是%s"%(a//b))
# print("余数是%s"%(a%b))



"""
等差数列：
1,3,5,7
差 2

a1 + (n—1)d
"""

a = int(input("请输入等差数列第一个数"))
b = int(input("请输入等差数列第二个数"))
c = int(input("请输入你想要的第几个数"))
result = a + (c-1) * (b - a)
print(result)


"""
123转化为321




bai = 123 // 100  = 1
tmp = 123 %  100  = 23
shi = tmp  // 10   = 2
ge  = tmp  %  10   = 3

result = ge * 100 + shi * 10 + bai



 


"""