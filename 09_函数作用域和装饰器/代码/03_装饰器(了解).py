# 装饰器：
#     作用是在其他函数的前面或后面添加功能，但是****不修改原函数****
"""
def swim():
    print('我爱游泳')


def swim2():
    print('先跳个舞')
    swim()
    print('再唱个歌')
"""

# 上面的方式有缺陷：****只能给swim添加功能****
"""
def run(x):
    print('我爱跑步')


def run2(fn):
    print('先跳个舞')
    fn(2)
    print('再唱个歌')


run2(run)
run2(swim)
print('*' * 100)
"""


# 上面还有缺点：调用的方式会发生变化
#    不使用装饰器就调用 run()
#      使用装饰器就调用 run2()


# 标准装饰器
# 定义装饰器

def outer(fn):
    def inner():
        print("先跳个舞")
        fn()
        print("唱歌")

    return inner


def sleep():  # 给这个函数装饰， 先跳舞，在唱歌
    print('sleep')


# sleep = outer(sleep)  # 装饰器的原理
# print(sleep.__name__)
# print('------')
# sleep()  # sleep ==> inner

@outer  # sleep = outer(sleep) 添加装饰器的语法
def sleep2():
    print('sleep2')


print(sleep2.__name__)
sleep2()

print('--------------------------------')
# 练习：写一个装饰器，计算函数运行的时间
import time

# 装饰器
def dec(fn):
    def cal(*args, **kwargs):  # 通用装饰器 通用参数， 可以接收任意参数
        start = time.time()
        fn(*args, **kwargs)
        end = time.time()
        print(end - start)

    return cal

"""
调用过程
dec(fn33)(n) ---> cal(*args, **kwargs) 
--> fn(*args, **kwargs) --> fn33(n)
"""
@dec
def fn33(n):
    s = 0
    for i in range(n):
        s += i
    print(f's:{s}')


# print(fn33.__name__)
fn33(10 ** 6)
