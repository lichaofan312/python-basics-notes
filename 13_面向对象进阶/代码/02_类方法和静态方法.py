# 类：
#    属性：类属性，对象属性，私有属性
#    方法：对象方法，私有方法， 类方法，静态方法

class Person:
    age = 30  # 类属性

    def __init__(self, name):
        self.name = name  # 对象属性

    #  对象方法 成员方法
    def run(self):
        print('run')
        print(self.name)
        print(self.age, Person.age)
        self.__sleep()

    def __sleep(self):
        print('sleep')


    """
    1.类方法可以用类名来调用（推荐），也可以用对象来调用
    #    2.类方法作用是：不需要创建对象(不需要消耗对象内存)，就可以直接使用类方法，可以节省内存
    #    3.类方法中有cls,没有self,表示可以去调用类名能调用的，不能调用对象属性，对象方法，私有属性，私有方法
    #      cls可以调用类属性，其他类方法，静态方法
    """
    @classmethod  # 类方法
    def eat(cls):  # cls: class  自动接收一个类名 cls: Person
        print('eat')
        print(cls == Person)
        print(cls.age)

    """
    #    1.静态方法可以用类名来调用（推荐），也可以用对象来调用
    #    2.静态方法作用是：不需要创建对象(不需要消耗对象内存)，就可以直接使用静态方法，可以节省内存（类名来调用）
    #    3. 既没有cls，也没有self，静态方法内部不需要调用类中的任何属性和方法
    """

    @staticmethod
    def game():
        print('game 静态方法')


p = Person('邓超')
"""
run
邓超
30 30
sleep
"""
# p.run()
# p.eat() # 不建议用对象去调用 True
Person.eat()  # True

Person.game()
p.game()

# 类方法: (掌握)
# @classmethod
#    1.类方法可以用类名来调用（推荐），也可以用对象来调用
#    2.类方法作用是：不需要创建对象(不需要消耗对象内存)，就可以直接使用类方法，可以节省内存
#    3.类方法中有cls,没有self,表示可以去调用类名能调用的，不能调用对象属性，对象方法，私有属性，私有方法
#      cls可以调用类属性，其他类方法，静态方法

# 静态方法:（了解）
# @staticmethod
#    1.静态方法可以用类名来调用（推荐），也可以用对象来调用
#    2.静态方法作用是：不需要创建对象(不需要消耗对象内存)，就可以直接使用静态方法，可以节省内存（类名来调用）
#    3. 既没有cls，也没有self，静态方法内部不需要调用类中的任何属性和方法
