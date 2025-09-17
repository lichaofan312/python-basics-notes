# 作用域：变量起作用的范围
#   函数有作用域
a = 10  # 全局作用域


def fn():
    b = 20  # 局部变量 局部作用域
    print(f'b:{b},a:{a}')


print(fn())

# 函数嵌套
# 内建作用域 B： Built-in
# 全局作用域 G： Global
# 函数作用域 E： EnClosing
# 局部作用域 L： Local
import math

print(math.pi)  # 内建作用域
x = 3  # 全局作用域


def fn1():
    y = 4  # 函数作用域

    def fn2():
        z = 5  # 局部作用域


# 关键字： global，
# global 全局
m = 10


def f1():
    # 如果 修改 全局的变量
    # m += 4  # 定义了一个新的m 变量
    global m
    m += 4  # 定义了一个新的m 变量
    print(m)


f1()  # 4
print(m)  # 10

# 关键字 nonlocal
A = 3


def f2():
    A = 4  # 函数作用域

    def f3():
        # global A # 如果声明 使用global A 那么就使用全局变量的A
        nonlocal A
        A = 5  # 局部作用域
        print(f'f3 A:{A}') # f3 A:5

    f3()
    print(f'f2: A:{A}') # f2: A:5


f2()  # f3 A:5
print('函数外的值A:', A)  # 函数外的值A: 3
