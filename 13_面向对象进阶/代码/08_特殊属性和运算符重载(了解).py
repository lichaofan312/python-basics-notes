# __slots__ : 了解,扩展

class Person:
    # 限制你的属性名 只能使用这三个 提供了属性名的列表，
    # 必须包含在这个列表中
    __slots__ = ['name', 'age', 'sex']

    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person('小明', 10)
p.sex = "男"  # 给对象p添加一个属性
print(p.name, p.age, p.sex)


# p2 = Person('小黑', 30)
# print(p2.name, p2.age)


# 特殊属性：了解
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('跑步')


d = Dog('旺财', 3)

print(d.__class__)  # <class '__main__.Dog'>
print(Dog.__class__)  # <class 'type'>
print(d.__dict__)  # 字典 {'name': '旺财', 'age': 3}

d2 = Dog(**{'name': '旺财1', 'age': 3})
d2 = Dog(name='旺财1', age=3)  # 等价

print(d2.__dict__)


# print(d.__module__)  # 模块 ‘__main__’

# 魔法方法，一般会自动调用
# __new__() : 创建对象 (先调用)
# __init__() : 初始化（然后调用）
# __del__() : 对象删除时调用（最后调用）


# 运算符重载: 扩展
class Number:
    def __init__(self, n):
        self.n = n

    # 运算符重载: 了解
    def __add__(self, other):
        return self.n + other.n

    # __str__ : 让打印对象的内容 n1 变成__str__函数的返回值 f' -- {self.n} -- '
    # 不写 打印地址
    # def __str__(self):
    #     return f' -- {self.n} -- '

    # 可以打印写在列表中的内容
    def __repr__(self):
        return f' ** {self.n} ** '


n1 = Number(3)
n2 = Number(4)
print(n1 + n2)  # 7
print('*' * 100)
# print(n1)  # __str__(self)
print([n1, n2])
