# 逻辑运算符
#   and与(且)  or或者  not非（取反）

# and: 并且
#   2边都为True则为True，只要有一个是False 则为False
print(True and True)
print(False and True)
print(True and False)
print(False and False)
print(3 and 5)  # 5
print('------------')
# or：或者
#   2边都为False则为False, 只要有一个是True则为True
print(True or True)
print(False or True)
print(True or False)
print(False or False)

print('------------')
# not 非，取反
print(not True)  # False
print(not False)  # True
print(not 0)  # True
print(not None)  # True
print(not "")  # True
print(not [])  # True
print(not ())  # True
print(not {})  # True

# 不同数据类型 隐式bool值 判断
#   数字类型： 0是假，其他为真
#   字符串类型： 空字符串''为假，其他为真
#   bool类型： False为假，True为真
#   NoneType类型: None是假
#   list类型：空列表[]是假，其他为真
#   tuple元组： 空元组()为假,其他为真
#   dict字典：空字典{}为假，其他为真
'''
print(bool(0))
print(bool(''))
print(bool(None))
print(bool([]))
print(bool(()))
print(bool({}))
'''
print()

# 扩展: and和or的短路运算

# and:
#  从左往右依次判断每一个数，只要有一个是False（bool值隐式判断） 则返回该数
print(0 and 5)  # 0
print(3 and 5)  # 5
print(3 and 0 and 5)  # 0
print('-----')
print(3 and 0 and print(5))  # 0
print('---------')
print(3 and print(5) and 6)  # None

print('---------')
# or:
#  从左往右依次判断每一个数，只要有一个是True（bool值隐式判断） 则返回该数
print(0 or 666)  # 666
print(0 or print(8) or 888)  # 8 888
print(0 or 888 or print(8))  # 888
print('------------------')

# 练习：请直接写出答案（先不要运行）
x = True and 6  # x = 6
y = False or True or 8  # y = 1
z = x * 3 + y * 2  # 6*3 + 1*2 = 20
print(x, y, z)  # 6 True 20
