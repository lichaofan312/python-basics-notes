# Python数据类型:
#  int, float, str, bool, NoneType,
#  list, tuple, dict, set(了解), bytes

# list列表 : Array数组
# 为什么要使用列表：
# 举例：如果我们表示汽车品牌用变量保存单个值
a = "BYD"
b = "五菱宏光"
c = "小米"
d = "蔚来"
e = "法拉利"
f = "兰博基尼"
g = "路虎"

# 如果要你表示300个品牌, 变量就太多了，这时我们可以使用列表来表示：
cars = ["BYD", "五菱宏光", "小米", "蔚来", "蔚来", "法拉利", "兰博基尼", "路虎"]

# 列表的基本功能
# 1.列表定义
nums = [10, 20, 30, 40, 50]

# 2.索引,下标
#   从0开始
print(nums[0])
print(nums[1])
print(nums[2])
print(nums[3])
print(nums[4])

print()

# 3.长度,元素个数
print(len(nums))
print()
# 4.遍历,循环
for num in nums:
    print(num)

for i in range(len(nums)):
    print(nums[i])

for i, n in enumerate(nums):
    print(i, n)
print()
# 5.修改列表
nums[0] = 5
print(nums)
print()

# 6.切片 (很重要) : 不会修改原列表
#    list[start : stop : step] : [start, stop)
#  和range(start, stop, step)类似  [start, stop)
ages = [10, 20, 30, 40, 50, 60, 70, 80]
print(ages[:5])  # 0，1，2，3，4 索引的值
print(ages[5:])  # 5 之后的索引 值
print(ages[2:5])  # 5 之后的索引 值
print(ages[2:8:2])  # 5 之后的索引 值
print(ages[7:1:-1])  # 5 之后的索引 值
print(ages[::-1])  # 倒序

# 7. 合并 +  (了解)
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
# 8. 重复 * (了解)
print(a * 3)

# 9. 成员 in (掌握)
if 3 in a:
    print('3在列表a 中')

# 需求: 列表去重 (掌握)
nums = [1, 2, 3, 4, 5, 6, 7, 7, 7, 8]
nums2 = []
for n in nums:
    if n not in nums2:
        nums2.append(n)  # 把n 添加到nums2列表中
print(nums2)
# 10.删除元素 del (了解)
nums = [10,20,30,40,50]
del nums[0]
del nums[:]
print(nums)
