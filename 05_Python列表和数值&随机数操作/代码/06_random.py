# random: 随机数

# import keyword
# import math
# import time
import random

# random.choice(): 从列表/str中随机取一个元素
# random.randint(a, b): 从一个范围随机取一个整数，闭区间
# random.randrange(a, b, step): 随机获取一个奇数，和range类似
# random.random() : 在0~1之间[0,1)随机获取一个小数

# random.uniform(3, 5) ： 3~5之间的小数 （了解）
# random.shuffle(list) : 随机打乱顺序  （了解）

girl_friends = ["刘亦菲0", "迪丽热巴", "刘亦菲1", "刘亦菲2", "刘亦菲3", "刘亦菲4"]
print(random.choice(girl_friends))  # 刘亦菲3  从列表/str中随机取一个元素
print(random.choice("abc"))  # a  从列表/str中随机取一个元素
print(random.choice(range(1, 7)))  # 3  从列表/str中随机取一个元素

print(random.randint(3, 5))  # [3,5] 从一个范围随机取一个整数，闭区间

print(random.randrange(3, 4))  # [3,5)
print(random.randrange(2, 9, 2))  # 2,4,6,8 取值
print(random.random()*50)  # 0,1 之间 取小数
print(random.uniform(3, 5))  # 【3，5） 之间取小数
print(random.uniform(3, 3))  # 【3，3】 之间取小数

nums = [1,3,2,4,6,7,8,3]
random.shuffle(nums)  # 随机打乱顺序
print(nums) # [6, 2, 7, 3, 3, 8, 4, 1]