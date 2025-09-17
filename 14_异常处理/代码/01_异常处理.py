# 异常处理

# 错误：代码还没运行就已经出错了，这种情况要先解决
# 异常：代码写的时候不报错，运行报错


# 异常处理：针对有一定概率(小概率)出现异常的，我们需要做异常处理
# try-except:
#   尝试执行try中的代码，如果出错则进入except，否则不进入
#   作用是：防止报错导致程序结束，出现的错误可以被except捕获

# a = 0
# n = 3 / a  # ZeroDivisionError: division by zero 直接中止程序 明显的异常需要去捕获
# print(n)
"""
#  方式一
try:
    a = 0
    n = 3 / a
    print(n)  # 1.5
except:
    print('报错了')  # 报错了

print('报错了，依然会执行')  # 报错了，依然会执行
"""
"""
#  方式二
try:
    a = 0
    n = 3 / a
    print(n)
except Exception as e:  # Exception 异常类的父类
    print(e)  # division by zero
    print(type(e))  # <class 'ZeroDivisionError'>
    print('出错了')
"""

"""
try:
    a = 2
    n = 3 / a
    print(n)
    l = []
    print(l[0])
except ZeroDivisionError as e:  # Exception 异常类的父类
    print(e)  # division by zero
    print(type(e))  # <class 'ZeroDivisionError'>
    print('出错了')
except IndexError as e:
    print(e) # list index out of range
    print('出错了， IndexError') # 出错了， IndexError
"""
# try-except-else
#   try尝试执行代码，如果出错了就进入except,否则进入else
"""
try:
    a = 3
    n = 3 / a
    print(n)
except Exception as e:  # Exception 异常类的父类
    print('出错了', e)
else:
    print("没有问题")
"""
# try-except-finally
#    try尝试执行代码，如果出错了就进入except, 最终进入finally(不管有没有错)
try:
    a = 0
    n = 3 / a
    print(n)
except Exception as e:  # Exception 异常类的父类
    print('出错了', e)
finally:
    print("不管有没有错误， 都需要处理")

# Python自带的异常类型:
#     AttributeError : 属性错误
#     NameError: 变量没定义
#     IndexError : 索引越界
#     ZeroDivisionError : 除以0的错误
#     KeyError : 字典的key错误
#     FileExistsError : 文件已经存在
#     FileNotFoundError : 文件不存在
#     ImportError : 导包错误
#     IndentationError : 缩进错误
#     SyntaxError : 语法错误
print("*" * 100)
# 2. 主动抛出异常
try:
    raise NameError('sorry, 我错了')
except Exception as e:
    print('------------出错了', e)
finally:
    print("执行")

print("*" * 100)


# 3. 断言
def fn(n):
    try:
        # 判定n 不等于 0 ，否则抛出异常
        assert n != 0, "报错了， n 不能为0"
        print(5 / n)
    except Exception as e:
        print('出错了 ', e)


fn(0)
