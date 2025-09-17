''' '''

# 包 package : 是一个有__init__.py文件夹
# 模块 module: 是一个python文件

# 封装思路: 项目 => 包(文件夹) => 模块(python文件) => 类 => 函数 => 代码

# 创建包
# 创建模块

print("--------导入模块-----精确导入---")
# 导入模块
#   import
#   from - import
from time import sleep  # 精确导入

sleep(2)  # 直接用
print("sleep(2)")

print("----导入模块----模糊导入--------")
# 模糊导入 : * 表示所有内容
from requests import *  # 模糊导入

# 自定义模块

print("--------自定义模块 当前模块处于同一目录--------")
import module1  # 导入的时候 会自动加载 打印 我是模块1 单例模式，只会加载一次
import module1  # 导入的时候 会自动加载

print(module1.name) # ikun
module1.f()
"""

"""
from module1 import name,f

print(name)
# print(module1.name) # 精准导入， 就会报错
f()

print("--------模块在包里面 使用--------")
# 模块在包里面
#  导入方式1

print("--------导入方式1--------")
from package1 import  module2
print(module2.name)

#  导入方式2

print("--------导入方式2--------")
from package1.module2 import  name
print(name)

print("--------使用别名: as 改名后只能用别名--------")
# 别名: as 改名后只能用别名
import pandas as pd
import module1 as m1
print(m1.name)

from package1 import module2 as m2
m2.f()

