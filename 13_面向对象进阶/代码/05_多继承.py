# 单继承： 只有1个父类
# 多继承： 多个父类 （了解）
class Father:
    def __init__(self, name):
        self.name = name

    def smoke(self):
        print('smoke')


class Mother:
    def __init__(self, age):
        self.age = age

    def cook(self):
        print('cook')


class Son(Father, Mother):
    def __init__(self, name, age, sex):
        """
        # Father.__init__(self, name)  # 显式调用 但不推荐
        # Mother.__init__(self, age)
        """

        """
        # super().__init__(age)  # 'Son' object has no attribute 'age'
        # super().__init__(name)  # 默认
        """

        # 继承链 : Son 先继承Father, 在继承Mother 是有顺序的，注意
        # super(Son, self).__init__(name)  # 调用 Father 的构造函数
        super().__init__(name)  # 隐式调用
        super(Father, self).__init__(age)  # 然后再在Father 继承链上 找 Mother
        self.sex = sex

    def game(self):
        print('game')


son = Son('小红', 20, '男')
print(son.name, son.age, son.sex)
son.cook()
son.smoke()
son.game()
# 2个父类： 父亲，母亲
# 1个子类： 儿子
# 继承链 有顺序
print(Son.__mro__)

"""
(<class '__main__.Son'>, 
<class '__main__.Father'>, 
<class '__main__.Mother'>, 
<class 'object'>)
"""
