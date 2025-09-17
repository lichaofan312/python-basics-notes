# 面向对象的4大特征：
#   1. 封装：属性和方法
#   2. 继承：子类可以继承父类的属性和方法
#   3. 多态
#   4. 抽象


# 继承：子类继承父类的属性和方法
#    方便后期维护代码

# 单继承 ： 只有1个父类

class Ipad:
    def __init__(self, color, price):
        self.color = color
        self.price = price

    def movie(self):
        print('movie')


class Iphone(Ipad):
    def __init__(self, color, price, size):
        # 一定要写父类的调用
        super().__init__(color, price)  # 调用父类的init 方法 来初始化 color price
        # Ipad.__init__(self, color, price) #方式二 借用父类的构造函数
        self.size = size

    def call(self):
        print('call')


iphone16 = Iphone('红', 8000, 6)
print(iphone16.color, iphone16.price, iphone16.size)
iphone16.movie()


# 继承的使用场景：
# 1 子类在父类的基础上， 额外扩展功能
# 2 将不同子类的公共属性和方法，提取出来，成为一个父类
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(self.name, "sleep")


class Dog(Animal):
    def __init__(self, name, age, sex):
        super().__init__(name, age)
        self.sex = sex

    def eat(self):
        print('吃肉')


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def catch_mouse(self):
        print('catch_mouse')


dog = Dog('小黄', 2, 'male')
cat = Cat('米米', 3, '白色')

dog.sleep()
dog.eat()
cat.sleep()
cat.catch_mouse()
