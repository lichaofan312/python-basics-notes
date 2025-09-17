# self:
#   1.不是关键字, 只是一个形参，但是建议写self, 不需要给self传值
#   2.self是指向当前类的对象（哪个对象调用函数，则该函数中的self就是这个对象）
#   3.作用是让你可以在函数中调用类中的其他属性或方法
class Dog:
    def __init__(self, name):  # self ==> dog1
        self.name = name
        print("__init__中的self: ", id(self))  # __init__中的self:  2150324080976 2470237672080

    def eat(self):
        print(f"{self.name}喜欢吃骨头")
        print("eat 中的self: ", id(self))  # eat 中的self:  2150324080976 2470237672080


dog = Dog("旺财")
print('id(dog):', id(dog))  # id(dog): 2150324080976
dog.eat()
print("*" * 100)
dog1 = Dog("旺财1")
print('id(dog):', id(dog1))  # id(dog): 2470237672080
dog1.eat()
