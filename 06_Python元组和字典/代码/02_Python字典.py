# 字典 dict  dictionary字典

# dict特点：
#   1. 字典的key不能重复 （key 唯一性）
#   2. 字典的key不可以是 可变类型(list,dict,set)，但是建议使用字符串
#   3.  key无序性

# 1.创建
#  key:value ：键值对
dic = {'name': "张三", 'age': 100, (1, 2): 5}
print(dic)
# 2.索引 : 没有数字索引，但是可以使用key

dic = {'name': "张三", 'age': 100}
print(dic['age'], dic.get('age'), dic.get("age1"))
print(list(dic.keys()))
print(list(dic.values()))

# 推荐的方式
for key in dic:
    print(key)

for key in dic.keys():
    print(key)

print()
for k, v in dic.items():
    print(k, v)
# 3.长度
print(len(dic))

# 4.遍历


# 5.修改元素


# 6.切片: 不可以
# dict 没有数据索引，  而且dict 是无序的，
# 7.合并


# 8.重复： 不可以
# print(d1 * 3)

# 9.成员 (掌握)


# 字典的功能
# 增删改查
#  增，改


# 删：
#  pop(key): 删除key对应的元素 (掌握 )
#  clear() : 清空字典 （了解）
#  popitem() : 删除一个元素 （了解）
