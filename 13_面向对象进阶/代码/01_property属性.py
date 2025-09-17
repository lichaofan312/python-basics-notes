class Girl:
    def __init__(self, name, age):
        #  公有属性
        self.name = name
        #  私有属性
        self.__age = age

    # 公有方法
    def dance(self):
        print(f'{self.name}今年{self.__age}岁了， 会跳舞了')
        self.__sing()

    #  私有方法
    def __sing(self):
        print(f'{self.name}会唱歌')


g1 = Girl("刘亦菲", 18)
print(g1.name)
# 'Girl' object has no attribute '__age' 隐藏 私有属性不可以在类外部调用
# print(g1.__age)

g1.dance()


# g1.__sing() # 私有方法不可以在类外部调用

# 扩展 调用私有方法 _类名__属性
# print(g1._Girl__age) # 但不建议使用
# g1._Girl__sing()


# 作用是让 函数可以变成属性的方法来调用
#   1.必须有返回值， 2.没有参数
# @property  # (掌握)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # 快速计算的返回 一般用于返回私有属性的值
    # 1.必须有返回值， 2.没有参数
    #  getter 方法， 用于后取值
    @property
    def age(self):
        print('取值-----')
        return self.__age

    @age.setter  # 用于修改值
    def age(self, new_age):
        print('----赋值')
        self.__age = new_age


p = Person('张三', 18)
print(p.age)
p.age = 18
print(p.age)
