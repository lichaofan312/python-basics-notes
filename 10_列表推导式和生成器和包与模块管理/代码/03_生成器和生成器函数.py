# 生成器 generator (掌握)
#  需要使用next或者for循环来调用
import time

nums = [i for i in range(1, 6)]
print(nums)

g = (i for i in range(1, 6))  # 生成器
print(g)  # <generator object <genexpr> at 0x000001FDC04B8040> 用的时候不可以直接使用
# print(list(nums)) # 不推荐使用 可以用列表推导式

print("手动使用next ---------------------")
#  1 next
print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # 3
print(next(g))  # 4
print(next(g))  # 5
# print(next(g)) # 停止迭代 报错

print("自动使用next ---------------------")
# for
g1 = (i for i in range(1, 4))
for i in g1:
    print(f'i:{i}')  # 自动使用next

# 生成器函数:
#   1. 函数内部要有 yield
#   2. 需要用 next 来调用
#   3. 每个next都会在yield处暂停
#   4. yield 会暂停, 可以返回值

print("普通函数---------------------")


def fn():
    print('fn, 我会执行吗？')


# fn()

print("生成器函数---------------------")


def gfn():
    print('fn, 我会执行吗？')
    yield 666  # 改造变成生成器函数 会暂停, 可以返回值 类似return 的返回值，但是不会结束函数
    print('BBBB')
    yield 888


# 变成生成器函数之后，不会执行代码， 会返回一个参数
g = gfn()  # 进程已结束，退出代码为 0 但是没有执行
"""
<generator object gfn at 0x0000021ACBC34AC0>
fn, 我会执行吗？
666
"""
print(g)  # <generator object gfn at 0x000001F38FB84AC0>
print(next(g))  # 需要执行 就需要调用next(g) 执行第一个yield 同时 666 会返回

"""
BBBB
888
"""
print(next(g))  # 需要执行 就需要调用next(g) 执行第二个yield 同时 888 会返回

print("生成器函数---------------------")

print("生成器函数 手动使用next---------------------")


def gen():
    g = (i for i in range(1, 10 ** 100))

    for i in g:
        # 一个个返回值, 不会退出函数
        yield i


g = gen()
print(next(g))  # 调用next for 循环执行一次 执行第一个yield 同时 1 会返回

# print(next(g))
# print(next(g))

print("生成器函数 手动使用next---------------------")

# 练习
# 1.请写一个生成器函数, 得到前20个斐波那契数 (难度:*****)
# 斐波那契数列如下：0,1, 1, 2, 3, 5, 8, 13, 21, 34, 55...
#    提示:使用while True, 通过调用n次next来获取前20个数
# f(n) = f(n-1) + f(n-2)
# n<=2 return 1
#  斐波那契数
"""
def fun():
    a = 0
    b = 1
    while True:
        a, b = b, a + b
        yield a


import time

g1 = fun()
for i in range(20):
    time.sleep(2)
    print(next(g1), end=" ")  # 0,1, 1, 2, 3, 5, 8, 13, 21, 34, 55
print()
"""

print('一个生成器函数, 得到前20个斐波那契数--------------')


def f(n):
    if n <= 2:
        return 1
    return f(n - 1) + f(n - 2)


"""
def g1(num):
    g = (f(i) for i in range(1, num + 1))

    for result in g:
        yield result

g10 = g1(10)
count = 1
while count <= 10:
    time.sleep(1)
    #  1, 1, 2, 3, 5, 8, 13, 21, 34, 55
    print(next(g10), end=" ")
    count += 1
"""

def g2(num):
    for i in range(1, num + 1):
        yield f(i)

num = int(input("请输入一个数："))
i = 1
g = g2(num)
while i <= num:
    time.sleep(1)
    print(next(g), end=" ")
    i += 1
print()
print('一个生成器函数, 得到前20个斐波那契数--------------')
