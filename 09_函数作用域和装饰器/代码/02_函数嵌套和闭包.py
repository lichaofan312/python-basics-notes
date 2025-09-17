# 函数名称：既是函数名，也是指向该函数的变量
#          只要是指向该函数，就可以调用该函数

# 函数嵌套
"""
def f1():
    print('f1')

f1()
f2 = f1
f2()
"""


def fn():  # 1  函数套函数，
    def fn2():
        print("fn2 执行")

    return fn2  # 2  把内部函数返回


fn()()
print(fn().__name__)  # 说明真实指向的是fn2 函数


# 闭包：函数嵌套，且返回内部函数 就会形成闭包  (了解即可)
#       函数作用域中的变量 x=10 不会被释放
def fn3():
    x = 10 # 函数作用域

    def fn4():
        nonlocal x # 函数作用域中的变量 x=10 不会被释放
        x += 1
        print(f'fn4 x:{x}')

    return fn4

f4 = fn3()  # f4 == fn4
f4() # fn4 x:11
f4() # fn4 x:12
f4() # fn4 x:13
