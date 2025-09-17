''''''


# 理解面向对象
# 示例： 小狗吃食物（闻一闻smell、舔一舔lick、咬一咬bite）
# 	  分别采用面向过程和面向对象来分析
#
# 面向过程:  先闻一闻, 然后再舔一舔, 最后再咬一咬 (注重过程)
# 面向对象:  小狗是一个对象, 它可以闻一闻食物, 可以舔一舔食物, 可以咬一咬食物.(不注重过程, 注重对象)

# 1. 面向过程:  先闻一闻, 然后再舔一舔, 最后再咬一咬 (注重过程)
def smell():
    print('闻一闻')


def lick():
    print('舔一舔')


def bit():
    print('咬一咬')


smell()
lick()
bit()


# 2. 面向对象:  小狗是一个对象, 它可以闻一闻食物, 可以舔一舔食物, 可以咬一咬食物. (不注重过程, 注重对象)
class Dog:
    #  属性
    name = "旺财"

    #  函数 方法， 功能
    def smell(self):
        print(self.name, "闻一闻")

    def lick(self):
        print(self.name, "舔一舔")

    def bit(self):
        print(self.name, "咬一咬")


dog = Dog()
dog.smell()
dog.lick()
dog.bit()
