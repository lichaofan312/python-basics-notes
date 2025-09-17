# 类和对象
#   类是对象的抽象，class, 同一类事物的统称
#   对象是类的具体，object, 需要通过类来创建
#
#   类：不占内存
#   对象：占内存，不同对象占不同内存

#   类          对象
#   人          我
#  电脑       你的那台华为电脑
#  华为电脑   你的那台华为电脑
#  男朋友     你的男朋友


# 自定义类
#   所有的类都会继承object
class Person(object):
    # 属性 变量 类属性 使用类名来调用
    # *** 静态的，表示特征 名字， 年龄，身高，性别等
    # name = "jack"
    # age = 30

    # 方法 构造方法
    #  1 作用初始化属性值
    #  2 会在创建对象时， 自动调用
    def __init__(self, name, sex):
        #  成员属性， 对象属性， 用对象来调用
        self.name = name
        self.sex = sex

    # 动态特征 功能 函数
    def run(self):
        print(self.name, "跑步")


p = Person('杰伦', '男')
print(p.name, p.sex)  # 杰伦 男
p.run()  # 杰伦 跑步

p2 = Person('昆凌', '女')
print(p2.name, p2.sex)  # 昆凌 女
p2.run()  # 昆凌 跑步


# 一个类可以创建任意多个对象
# 比如：工厂生产华为手机的模型就是类
#      生产的每一部具体的手机就是一个对象


# 练习
# 1.创建Phone类
#      属性：color, size, price
#      方法：call, play_game, chat
class Phone:

    def __init__(self, color, size, price):
        self.color = color
        self.size = size
        self.price = price

    def call(self):
        print("call")

    def play_game(self):
        print("play_game")

    def chat(self):
        print("chat")


phone1 = Phone('绿色', "16", 3000)
print(phone1.color, phone1.size, phone1.price)
phone1.call()


# 2.小美在朝阳公园溜旺财【注：旺财是狗】
#   类People：
#       属性：姓名 name
#       方法：溜旺财 walk_dog
#            def walk_dog(self, place, dog_name):
#                   小美 在 朝阳公园 溜 旺财
class People1:
    def __init__(self, name):
        self.name = name

    def walk_dog(self, place, dog_name):
        print(f'{self.name}在{place}溜{dog_name}')


p3 = People1('小美')
p3.walk_dog("朝阳公园", "旺财")
