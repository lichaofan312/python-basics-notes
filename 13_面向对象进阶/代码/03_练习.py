# 练习
# 创建一个工具类Number，其中：
# 类属性：num  初始值为10
# 类方法：add_num(cls)  让num加1
#        sub_num(cls)  让num减1
#        mul_num(cls, n) 让num乘n
#        div_num(cls, n) 让num除n
# 静态方法：
#        add(x, y) : 求x+y的结果并返回
#        sub(x, y) : 求x-y的结果并返回
#
#  不创建对象，分别调用这些方法，然后打印num
class Number:
    num = 10

    @classmethod
    def add_num(cls):
        cls.num += 1

    @classmethod
    def sub_num(cls):
        cls.num -= 1

    @classmethod
    def mul_num(cls, n):
        cls.num *= n

    @classmethod
    def div_num(cls, n):
        cls.num /= n

    # add(x, y): 求x + y的结果并返回
    #        sub(x, y) : 求x-y的结果并返回
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def sub(x, y):
        return x - y


Number.add_num() # 11
Number.add_num() # 12
Number.sub_num() # 11
Number.mul_num(10) # 110
Number.div_num(5) # 22
print(Number.num) # 22
print(Number.add(1, 3))
print(Number.sub(1, 3))
