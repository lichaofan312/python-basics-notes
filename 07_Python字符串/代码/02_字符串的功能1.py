# 字符串的功能

# count(): 计数,统计某子串出现的次数
s = "hello hello hello"
print(s.count('l'))  # 6 统计一个字符
print(s.count('ll'))  # 3 统计连续字符
print(s.count('ll', 8, 10))  # 1  在[8,10)之间查找"ll"出现的次数

# 大小写判断 (掌握)
# print('ABC'.isupper())  # 字母是否为大写
print('ABC'.isupper())
# print('abc'.islower())  # 字母是否为小写
print('ABC'.islower())  # False
# print('123'.isdigit())  # 是否为数字
print('123'.isdigit())  # True
# print('abcABC'.isalpha())  # 是否为字母
print('abcABC'.isalpha())  # True
# print('abcABC123'.isalnum())  # 是否字母或数字
# print('   '.isspace())  # 是否为空格字符串
# print('Hello World'.istitle())  # 是否每个单词首字母大写,其他小写
print('Hello World'.istitle())  # True

# 大小写转换
# print('abc123'.upper())  # "ABC123" 转成大写
print('abc123'.upper())
# print('ABC123'.lower())  # 'abc123' 转成小写
print('ABC123'.lower())
# print(int('123'))  # 转成整数 123
print(int(float('3.14')))
# print(float('3.14'))  # 转成小数 3.14
# # print('heLLO woRLd'.title())  # 转换成:每个单词首字母大写,其他小写
print('heLLO woRLd'.title())  # Hello World
# print('heLLO woRLd'.swapcase())  # 大小写切换: 大写变成小写,小写变成大写  'HEllo WOrlD'
print('heLLO woRLd'.swapcase())

# 查找
#   find(): 查找指定子串第一次出现的下标位置,如果不存在则返回-1
#  rfind(): 从右往左查找指定子串第一次出现的下标位置,如果不存在则返回-1
#   index(): 不用
#   rindex(): 不用
s = "ikun is very very very handsome"
print(s.find('very'))  # 第一个下标： 8
print(s.find('lcf'))  # 没有找到 -1
print(s.rfind('very'))  # 18 从右往左找
print(s.rfind('very1'))  # 没有找到 -1
# 练习:
# 1.已知字符串：“this is a test of Python”
s = 'this is a test of Python'

# a.统计该字符串中字母s出现的次数: count()
print(s.count('s'))  # 3

# b.取出子字符串“test”, 用切片,不能数: 使用find(),len()
print(s[s.find('test'):s.find('test') + len("test")])

# c.采用不同的方式将字符串倒序输出: 切片，循环
print(s[::-1])
print(list(range(len(s) - 1, -1, -1)))
for i in range(len(s) - 1, -1, -1):
    print(s[i], sep="", end="")
print()

# 拆分,合并,替换
# 拆分: 分割
#  split() : 拆分后得到列表
s1 = "ikun  is very very very handsome"
print(s1.split())  # ['ikun', 'is', 'very', 'very', 'very', 'handsome']
# print(s1.split(' ')) # ['ikun', 'is', 'very', 'very', 'very', 'handsome']
print(s1.split("ikun"))  # ['', '  is very very very handsome']

# splitlines(): 按行拆分
s2 = '''床前明月光,
疑是地上霜.
举头望明月,
低头思故乡.'''
print(s2.splitlines())  # ['床前明月光,', '疑是地上霜.', '举头望明月,', '低头思故乡.']
print(s2.split('\n'))  # ['床前明月光,', '疑是地上霜.', '举头望明月,', '低头思故乡.']
print(s2.splitlines(keepends=True))  # ['床前明月光,\n', '疑是地上霜.\n', '举头望明月,\n', '低头思故乡.']
print()

# 合并: join : 会得到字符串类型
#   将列表中的字符串拼接
n = ['床前明月光,', '疑是地上霜.', '举头望明月,', '低头思故乡.']
'''
床前明月光,
疑是地上霜.
举头望明月,
低头思故乡.
'''
print('\n'.join(n))  # 将列表每一个元素加起来
print('\t'.join(n))  # 床前明月光,	  疑是地上霜.	举头望明月,	低头思故乡.
print()

# 替换: replace() : 默认替换所有匹配的

s1 = "ikun  is very very very handsome"  # 字符串不可以变
s2 = s1.replace("very", "not")  # 返回新字符串
print(s2)

# 练习
# 1.已知字符串：“this is a test of Python”
# d.将其中的"test"替换为"exam" : replace()
ss = "this is a test of Python"
ss1 = ss.replace("test", "exam")
print(ss1)
# 2.去掉字符串123@zh@qq.com中的@;
# 提示: replace()  或者 split()+join()
email = "123@zh@qq.com"
print(''.join(email.split("@")))  # 123zhqq.com # 将列表每一个元素加起来
print(email.replace("@", "")) # 123zhqq.com
