# 使用场景：
#   while循环： ①无限循环， ②未知循环次数
#   for循环：一般使用在已知循环次数

# 打印1~100的每一个数
'''
i = 1
while i<= 100:
    print(i)
    i += 1
'''

# for-in循环：
#  每次循环，i会自动等于右边range中的每一个数
for i in range(1, 101):
    print(i)
print()

s = 0
for i in range(1, 101):
    s += i
print(s)

print()
# for循环使用场景
# 1.和range结合
#   比如：循环1~10，找到能被3整除的数
for i in range(1, 11):
    if i % 3 == 0:
        print(i)
print()

# 2.和列表结合
# 列表的基本操作
#  元素：列表中的每一个值
nums = [11, 22, 33]
# 索引 从0开始的一个整数
print(nums[0])
print(nums[1])
print(nums[2])
print(nums[-1])  # 倒数第一个元素
print()
print(len(nums))
print()
for num in nums:
    print(num)
print()
for i in range(len(nums)):
    print(nums[i], sep='-')
print()

for i, n in enumerate(nums):
    print(i, n)
# 还可以使用for的有：
#    range()
#    list: [1,2,3]
#    dict: {'name': 'ikun', 'age': 20}
#    tuple: (1,2,3)
#    set: {1,2,3}
#    str: "hello"
