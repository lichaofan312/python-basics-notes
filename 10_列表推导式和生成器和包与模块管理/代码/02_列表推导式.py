# 列表推导式: (掌握)
#    使用for循环用一行来生成列表
# 创建一个列表
print(list(range(1, 6)))

nums = [1, 2, 3, 4, 5]
nums2 = []
for i in range(1, 6):
    nums2.append(i)
print(nums2)
print()

num3 = [i for i in range(1, 6)]  # [1, 2, 3, 4, 5]
print(num3)

num3 = [i for i in range(1, 10) if i % 2 and i % 3 == 0]  # 得到奇数[3, 9]
print(num3)

num3 = [i for i in range(1, 10) if i % 2 if i % 3 == 0]  # 得到奇数 if 嵌套 #[3, 9]
print(num3)

num4 = [i + j for i in "ABC" for j in "123"]  # ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
print(num4)

# 字典推导式(了解)
d = {f'name{i}': i for i in range(1, 6)}  # {'name1': 1, 'name2': 2, 'name3': 3, 'name4': 4, 'name5': 5}
print(d)

# 集合推导式
d = {i for i in range(1, 6)}  # {1, 2, 3, 4, 5}
print(d)
