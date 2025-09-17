# 回调函数： 了解
#   把函数当作参数传入另一个函数中
"""
def fn(n, cb):
    print(f'n:{n}')
    return cb(n)


print(fn(3, lambda x: x ** 2))
"""


def cb(x):
    return x ** 2


def fn(n, cb):
    print(f'n:{n}')
    return cb(n)


print(fn(3, cb))

# filter(lambda x: x > 0, [1, -2, 3, -3, 4, -4])
"""
def filter1(condition, nums):
    list1 = []
    for i in nums:
        if condition(i):
            list1.append(i)
    return list1


results = filter1(lambda x: x > 0, [1, -2, 3, -3, 4, -4])
print(results)
print('-------------------')
"""

# sort(key=)
list1 = [
    {'name': '张三', 'age': 18, 'score': 50, 'tel': 18866669999, 'sex': '不明'},
    {'name': '李四', 'age': 16, 'score': 88, 'tel': 18866668998, 'sex': '男'},
    {'name': '王五', 'age': 17, 'score': 48, 'tel': 18866667995, 'sex': '女'},
    {'name': '陈一军', 'age': 61, 'score': 59, 'tel': 18866669998, 'sex': '不明'},
    {'name': '陈二军', 'age': 49, 'score': 88, 'tel': 18866669396, 'sex': '男'},
    {'name': '陈三军', 'age': 49, 'score': 61, 'tel': 18866668994, 'sex': '女'}
]
# 需求： 将上述list1 按照age 进行升序
list1.sort(key=lambda d: d['age'])  # 最终比较age
print(list1)

list1.sort(key=lambda d: d['score'], reverse=True)  # 最终比较age
print(list1)

# 按照数字进行升序
list2 = [
    ('张三', 18),
    ('李四', 16),
    ('王五', 17),
    ('陈一军', 61),
    ('陈二军', 49),
    ('陈三军', 48)
]

list2.sort(key=lambda t: t[1])
print(list2)
