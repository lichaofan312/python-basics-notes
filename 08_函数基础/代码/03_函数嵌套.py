# 函数嵌套（难点）

# 函数名称：既是函数名，也是指向该函数的变量（对象）
#          只要是指向该函数的变量，就可以调用该函数
def fn1(x):
    print(f'x:{x}')

    def fn2(y):
        print(f'y:{y}')

    return fn2


print(type(fn1(3)))  # <class 'function'>
f2 = fn1(5)
f2(9)

fn1(3)(8)

print("==============")


def fn4(x):
    print("fn3:", x)


fn4(1)
fn44 = fn4
fn44(1)

print("==============")


# 函数之间可以进行相互嵌套调用
def test():
    test1()
    print(11111)

def test1():
    test2()
    print(22222)


def test2():
    test3()
    print(33333)


def test3():
    print(44444)


test()
