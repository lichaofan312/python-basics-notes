# 私有属性不能继承：
#     私有属性只能在当前类内部使用

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    def eat(self):
        print('eat', self.__age)


class Boy(Person):
    def __init__(self, name, age, sex):
        super().__init__(name, age)
        self.sex = sex

    def sleep(self):
        # print('sleep', self.__age) # 子类也无法使用父类的私有属性
        print('sleep', self.age) # 子类也无法使用父类的私有属性


boy = Boy('小明', 20, '男')
print(boy.name)
# print(boy.__age) # 在类的外部不可以使用私有属性
# print(boy.age)  # 在类的外部不可以使用私有属性 只能调用属性方法
print(boy.sex)
boy.sleep()
boy.eat()
