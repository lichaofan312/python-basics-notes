# 文件操作:
#  1.打开文件
#  2.操作文件(读取read / 写入write)
#  3.关闭文件

# 1.打开文件
# open(file, mode='r')
#   file: 打开的文件路径
#   mode:
#     r : 只读read, 如果文件不存在则报错
#     rb: 只读二进制, 如果文件不存在则报错
#
#     w : 清空写write, 如果文件不存在会自动创建
#     wb: 清空写二进制, 如果文件不存在会自动创建
#     a : 追加写append, 如果文件不存在会自动创建
#     ab: 追加写二进制, 如果文件不存在会自动创建


# 文件句柄, 文件对象
# 读取
fp = open('a.txt', mode='r', encoding="utf-8")  # 不是二进制的都需要写encoding
print(fp.read())  # 读取所有内容
# print(fp.readline())  # 一次读一行， 会一直往下读
# print(fp.readline())
# print(fp.readlines()) # ['abcdef\n', 'hello']
# print(fp.read(3))  # abc 读取3个字符
# print(fp.read(3))  # def

# fp = open('a.txt', mode='rb')
# print(fp.read()) # b'abcdef\r\nhello\r\n\xe4\xbd\xa0\xe5\xa5\xbd' 需要手动解码
fp.close()

# 写
# fp = open('b.txt', 'w', encoding='utf-8')
# fp.write('hello 杰克')


# fp = open('b.txt', 'wb') # 清空写
# fp.write('hello 吗刻'.encode())  # 以二进制写入

# fp = open('c.txt', 'a', encoding='utf-8')
# fp.write("hello 鲁班七号\n")
# fp.write("hello 鲁班七号\n")
# fp.write("hello 鲁班七号\n")
# fp.write("hello 鲁班七号\n")
# fp.write("hello 鲁班七号\n")

fp = open('d.txt', 'ab')
fp.write("hello 码刻\n".encode())
fp.write("hello 诸葛亮\n".encode())
fp.close()

# with-as : 会自动关闭文件
with open('e.txt', 'a', encoding='utf-8') as fp:  # 出错也会文件关闭
    fp.write("Jeff \n")
    fp.write("Jeff \n")
    fp.write("Jeff \n")
