# 匿名函数： lambda
#   特点：
#       没有名字的函数
#       自带return
#       只表示一些简单的，有返回值的函数
def fn(x):
    return x ** 2


print(fn(3))

print("----------------------")
# ==> 匿名函数
f2 = lambda x: x ** 2
print(f2(3))

print("----------------------")
f3 = lambda x, y: x + y
print(f3(3, 4))
print("----------------------")
# 高阶函数
#  map: 映射，对列表做批量处理
n = map(lambda x: x ** 3, [1, 2, 3])
print(list(n))

n = map(lambda x, y: x * y, [1, 2, 3], [2, 3, 4])
print(list(n))

# filter: 过滤,找到符合要求的数据
n = filter(lambda x: x > 0, [1, -2, 3, -3, 4, -4])
print(list(n))
