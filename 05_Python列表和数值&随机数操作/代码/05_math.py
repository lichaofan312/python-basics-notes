# 数学操作

#    sum(): 求和
#    max()：最大值
#    min(): 最小值
#    round(): 四舍五入
#    abs(): 绝对值
#    pow(): 次方  (了解)


# math: 数学
import math

print(sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(sum(range(1, 101)))

print(max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(min([1, 2, 3, 4, -5]))

print(round(3.141567, 2))  # 保留2位

print(abs(-10))

print(pow(2, 3))  # 2**3

print(math.e)
print(math.pi)
print(math.inf)
print(math.sqrt(81), 81 ** 0.5)
print(math.factorial(5))  # 5的阶乘
print(math.ceil(3.14))  # 向上取整 4
print(math.floor(3.14))  # 向下取整 3
print(math.log(math.e))  # 1.0 log(e) = 1
print(math.log10(100))  # 2.0
print(math.sin(math.pi))  # 2.0
