# Python
#   不可变类型: int,float,str,tuple,bool,NoneType
#    可变类型: list, set, dict

# 赋值
# 不可变类型 (没有关联)
a = 10
b = a  # a, b 不可以变类型，所以没有关联
b = 20
print(f'a:{a}, b:{b}')  # a:10, b:20

# 可变类型 (有关联)
"""
a = [1,2,3]
b = a # 指向同一个列表 把地址给他了，
b[0] = 666
print(f'a:{a}, b:{b}') # a:[666, 2, 3], b:[666, 2, 3]
"""
# 深浅拷贝的可视化视图
#  http://pythontutor.com/live.html#mode=edit

# copy: 浅拷贝/浅复制 想让a,b 的值相互不影响， 修改了b, 不想影响a,
a = [1, 2, 3]
# b = a # 指向同一个列表 把地址给他了，
b = a.copy()  # a.copy() b 被分配了另外一个堆内存空间
b[0] = 666
print(f'a:{a}, b:{b}')  # a:[1, 2, 3], b:[666, 2, 3]

# deepcopy 深拷贝
a = [1, 2, [3,4]]
b = a.copy()  # a.copy() 浅拷贝， 针对二维列表，只是第一层拷贝 第二层不拷贝，也就是说第二层会指向同一块堆内存
b[2][0] = 666
print(f'a:{a}, b:{b}')  # a:[1, 2, [666, 4]], b:[1, 2, [666, 4]]

import copy
print('针对 二维列表')
a = [1, 2, [3,4]]
b = copy.deepcopy(a)  # copy.deepcopy(a) 深拷贝， 针对二维列表，第一层拷贝 而且 第二层也拷贝，也就是说第二层会指向不同一块堆内存
b[2][0] = 666
print(f'a:{a}, b:{b}')   # a:[1, 2, [3, 4]], b:[1, 2, [666, 4]]
