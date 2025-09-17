# 1. print输出,打印内容, 在控制台输出内容
print(200, 300, 400, sep='++')

# sep=" " 分隔符,默认是空格, 打印多个内容时的连接符号
# 可以查看Python函数源码: ctrl + 鼠标左键


# end="\n" 结束符,默认是\n表示换行符
#     \n : 表示换行
#     \t : 表示制表符
print(800, 900, 1000, sep='\n')

print(300, end='\t')
print(4000, end='----')
print(5000, end='\n')

# 练习: 打印以下内容,使用sep将唱,跳,rap连接
#     "唱+跳+rap"
print("唱", "跳", "rap", sep='+')

# 2.输入: input()
#  方便我们测试代码时自定义输入值
# Python中比较常见的3种类型: int整数, float小数, str字符串 "hello"

# 特点:
#    1.会让程序暂停,等待用户输入内容,且按enter键
#    2.input会得到一个str字符串类型,如果输入的是数字,则需要使用int或float来转换
# 快速添加或取消注释: ctrl + /

# name = input("请输入您的姓名：")
# print("获取到的名字： ", name)

# age = input("请输入您的年龄：")
# # print(age + 5) # can only concatenate str (not "int") to str
# print(type(age)) # 检测数据类型 <class 'str'>
# print(type(int(age))) # 可以将字符串转int
# print(float(age) + 5) # 15.0

# age = int(input("请输入您的年龄："))
# print(age + 5)

# 示例:
#    输入1个数,然后将这个数 乘以 3.14
result = float(input("请输入一个数:")) * 3.14
print(result)

# 练习:
# 1、输入1个名字, 用一个变量接收该名字，然后输出该变量的值
# 2、输入任意两个数字,计算他们的和

# 1、输入1个名字, 用一个变量接收该名字，然后输出该变量的值
name = input("请输入一个名字: ")
print("您的名字是：", name)

# 2、输入任意两个数字,计算他们的和
num1 = float(input("输入第一个数： "))
num2 = float(input("输入第二个数： "))
print("num1+num2 = ",num1 + num2)

