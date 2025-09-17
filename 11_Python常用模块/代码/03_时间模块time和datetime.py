import time

# time模块
#   time.time()  # 当前时间
#   time.sleep() # 暂停,休眠, 单位:秒
# 当前时间, 时间戳timestamp:从1970年1月1日0点到现在所经过的秒
# 1s = 1000ms 毫秒
# 1ms = 1000us 微秒
# 1us = 1000ns 纳秒
print(time.time())
time.sleep(0.1)

# datetime: 日期时间,
#   对time做了封装,比time更好用
#   date: 日期,表示年月日
#   time: 时间,表示时分秒
import datetime

# 1.创建日期对象
dt = datetime.datetime.now()  # 获取当前时间
print(dt)  # 2025-09-12 13:59:11.052163
dt = datetime.datetime(year=2030, month=2, day=4, hour=10, minute=30, second=30)
print(dt)  # 2030-02-04 10:30:30

# 2.日期的属性
print(dt.year, dt.month, dt.day, )
print(dt.hour, dt.minute, dt.second, )
print(dt.date())
print(dt.time())

# 3. 日期格式的转换
#   日期对象 : datetime对象
#   日期字符串 : "2030-02-01 12:30:20"
#   时间戳 :  1821025084.211286

# 日期对象 <==> 日期字符串
# strftime: 日期对象 => 日期字符串
# strptime: 日期字符串 => 日期对象
print(dt.strftime('%Y-%m-%d %H-%M-%S'))  # 2030-02-04 10-30-30
print(dt.strftime('%w'))

s = "2030-02-04 10-30-30"
dt2 = datetime.datetime.strptime(s, "%Y-%m-%d %H-%M-%S")
print(dt2, type(dt2))  # 2030-02-04 10:30:30 <class 'datetime.datetime'>

'''
> # %y 两位数的年份表示（00-99）
> # %Y 四位数的年份表示（0000-9999）
> # %m 月份（01-12）
> # %d 月内中的一天（0-31）
> # %H 24小时制小时数（0-23）
> # %I 12小时制小时数（01-12）
> # %M 分钟数（00-59）
> # %S 秒（00-59）

> # %a 本地简化星期名称
> # %A 本地完整星期名称
> # %b 本地简化的月份名称
> # %B 本地完整的月份名称
> # %c 本地相应的日期表示和时间表示
> # %j 年内的一天（001-366）
> # %p 本地A.M.或P.M.的等价符
> # %U 一年中的星期数（00-53）星期天为星期的开始
> # %w 星期（0-6），星期天为星期的开始
> # %W 一年中的星期数（00-53）星期一为星期的开始
> # %x 本地相应的日期表示
> # %X 本地相应的时间表示
> # %% %号本身
'''

# 日期对象 <==> 时间戳 (了解)
print(dt.timestamp())  # 1721028409.881082
print(datetime.datetime.fromtimestamp(1721028409.881082))  # 2024-07-15 15:26:49.881082

# 时间差 timedelta
d1 = datetime.datetime.now()

# 练习1: 求7天后的日期
curr_day = datetime.datetime(year=2030, month=2, day=4)
td = datetime.timedelta(days=7)  # 相差多少天
print(curr_day + td)  # 2030-02-11 00:00:00
# print(curr_day - td) # 2030-01-28 00:00:00

# 求2个日期相差多少天
d2 = datetime.datetime(2030, 10, 10)
d3 = datetime.datetime(2020, 3, 3)
d = d2-d3
print(d, type(d)) # # 3873 days, 0:00:00 <class 'datetime.timedelta'>
print(d.days) # 3873
print(d.days//365) # 10
