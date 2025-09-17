''' '''

# 循环结构：
#    while循环
#    for-in循环

# 循环10次
n = 1  # 循环起始值
while n <= 10:  # 循环的条件（结束条件）
    print(100)
    n += 1  # 循环的变量

print('------')

# 死循环：无限循环，循环不会停止
"""
while True:
    print("hello")
"""
#  死循环一般可以和input或time.sleep结合使用
# 需求：不断输入年龄，判断该年龄是否大于30
"""
while True:
    age = int(input("age:"))
    if age >= 30:
        print("中年人")
        break
    else:
        print("不达标")
"""

# 使用场景：
#  1. 无限循环
#  2. 可以是已知循环次数，也可以是未知循环次数

# 需求： 1+2+3+..+100
"""
n = 1
sum_ = 0
while n <= 100:
    sum_ = sum_ + n
    n += 1
print(sum_)
"""
# 练习：计算 10 的阶乘 : 1 * 2 * 3 * ...* 10
#   n的阶乘： 1*2*3*..*n
"""
total = int(input("请输入一个数(10)："))
n = 1
res = 1
while n <= total:
    res = res * n
    n += 1

print(f'{total}的阶乘:{res}')
"""
# 练习2：求1~100之间的能被6整数的数的和
"""
n = 1
sum_ = 0
while n <= 20:
    if n % 6 == 0:
        sum_ = sum_ + n
    n += 1
print(f"1~100之间的能被6整数的数的和:{sum_}")
"""
# 练习3：求1~100之间的奇数的个数
"""
n = 1
num = 0
while n <= 100:
    if n % 2 != 0:
        # print('n:{}'.format(n))
        num += 1
    n += 1
print(f"1~100之间的奇数的个数: {num}")
"""