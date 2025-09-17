# 迭代器 Iterator, list str
# 可迭代对象 Iterable

# type(): 查看数据类型
# isinstance() : 判断某个变量是否为某个数据类型


# 迭代器Iterator (了解)
#    1. 可以使用for循环遍历
#    2. 可以使用next调用

'''
print(isinstance(3, Iterator))  # False
print(isinstance(3.14, Iterator))  # False
print(isinstance("hello", Iterator))  # False
print(isinstance(None, Iterator))  # False
print(isinstance(True, Iterator))  # False
print(isinstance([1,2], Iterator))  # False
print(isinstance((1,2), Iterator))  # False
print(isinstance({1:2}, Iterator))  # False
print(isinstance({1,2}, Iterator))  # False
print(isinstance((i for i in range(3)), Iterator))  # True
'''
print(isinstance(10, int))
# print(type(10) == int)
print(isinstance(10, (int, float, list)))

# 可迭代对象 Iterable
#   1. 可以使用for循环遍历
'''
# print(isinstance(3, Iterable))  # False
# print(isinstance(3.14, Iterable))  # False
# print(isinstance("hello", Iterable))  # True
# print(isinstance(None, Iterable))  # False
# print(isinstance(True, Iterable))  # False
# print(isinstance([1,2], Iterable))  # True
# print(isinstance((1,2), Iterable))  # True
# print(isinstance({1:2}, Iterable))  # True
# print(isinstance({1,2}, Iterable))  # True
# print(isinstance((i for i in range(3)), Iterable))  # True
'''

# iter() : 可迭代对象 => 迭代器 (了解)
n = [1, 2, 3]
n2 = iter(n)
print(n2)
print(next(n2))
print(list(n2))  # [2, 3] 还原list
