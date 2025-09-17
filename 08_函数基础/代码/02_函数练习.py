# 1.封装一个函数 验证一个年是否是闰年
#   闰年的条件or：1. 能被4整除但是不能被100整除
# 			     2. 能被400整除
# 	条件1和条件2 满足一个即可
def isRunYear(year) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


"""
while True:
    print("闰年" if isRunYear(int(input("请输入一个年份： "))) else "平年")

"""


# 2.封装一个函数 获取指定月的天数
#   注意： 闰年和平年下  2月份的天数是不一样的
def days(year, month) -> int:
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    else:
        return 29 if isRunYear(year) else 28


print(days(2000, 2))


# 3.封装一个函数 获取指定月所属的季节:多分支
#   3、4、5春季 6、7、8夏季 9、10、11秋季  12、1、2冬季
def season(month) -> str:
    if month in (3, 5, 4):
        return "春季"
    elif month in (6, 7, 8):
        return "夏季"
    elif month in (9, 10, 11):
        return "秋季"
    else:
        return "冬季"


print(season(10))


# 4.封装一个函数 验证指定数是否是质数
# 注意：质数：在大于1的自然数中，除了1和它本身以外不再有其他因数的自然数。
def isPrime(num) -> bool:
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


print(isPrime(6))
