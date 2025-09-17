''''''
# 封装思路:
#    项目 => 文件夹(包) => 文件(模块) => 类 => 函数 => 代码

'''
问题: 代码重复
     后期维护成本太高
	 代码可读性不高

解决问题：函数
	在一个完整的项目中，某些功能会被反复使用，那么将这部分功能对应的代码提取出来，
	当需要使用功能的时候直接使用
	
本质：对一些特殊功能的封装

优点：
	a.简化代码结构，提高应用的效率
	b.提高代码复用性
	c.提高代码的可读性和可维护性

建议：但凡涉及到功能，都尽量使用函数实现
'''


# 函数定义 : def
def fn():
    print("i am function")


# 函数必须调用才会执行
fn()


# 一.函数的参数(必须要掌握)
#  形参: 形式参数
#  实参: 实际参数
def add(a, b):
    print(f'a:{a},b:{b}')
    return a + b


print(add(2, 3))


# 细分参数种类:
#  1. 必需的位置参数,
#  2. 默认参数,
def fn1(m, n, a=1, b=2):
    print(f'm:{m},n:{n}, a:{a},b:{b}')


fn1(3, 43, a=33)


#  3. 关键字参数, 一般和默认参数结合,


# 4. 不定长参数
#  *args: 接收任意多个位置参数, 元组 ()
#  **kwargs: 接收任意多个关键字参数, 字典 {}
def fn2(*args):
    print(type(args))
    print(args)


fn2(3)
fn2(3, 4)


def fn3(*args, **kwargs):
    print(type(args))
    print(type(kwargs))
    print(args)
    print(kwargs)
    print('---')


print('==============')
fn3(3)
print('==============')
print(fn3(3, 4, a=3, b=78))


# 二.返回值: return
#  1. return要写在函数内部, 返回 值
#  2. 如果不写return则默认会返回None
#  3. return会立刻结束函数,并返回值
def f4(a, b):
    return a + b


print(f4(1, 2))


# 函数参数顺序
#   形参顺序: 位置参数，*args,  默认参数，**kwargs
#   实参顺序: 位置参数，        关键字参数
def fn(a, b, *args, d=7, e=8, **kwargs):
    print(a, b, args)
    print(d, e, kwargs)


"""
2 3 ()
7 8 {}
"""
fn(2, 3)

"""
2 3 (4, 5)
77 88 {'f': 99, 'i': 100}
"""
fn(2, 3, 4, 5, d=77, e=88, f=99, i=100)


# 通用参数
def fun(*args, **kwargs):
    print(args, kwargs)

"""
(2, 3, 4, 5) {'d': 77, 'e': 88, 'f': 99, 'i': 100}
"""
fun(2, 3, 4, 5, d=77, e=88, f=99, i=100)

