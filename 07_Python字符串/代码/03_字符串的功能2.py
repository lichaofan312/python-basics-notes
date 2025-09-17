# 转义字符 \ : 让有语义的字符失去语义
# r'' : 让字符串中有语义的字符失去语义
# b'' : 字节
# f'' : f-string

s = 'F:\联昊电子\2025\9月份绩效\9月 任务\1 postman 调试MES'
print(s)  # F:\联昊电子5\9月份绩效\9月 任务 postman 调试MES
# \\ 表示一个斜杠  让有语义的字符失去语义
s = 'F:\联昊电子\\2025\9月份绩效\9月 任务\\1 postman 调试MES'
print(s)  # F:\联昊电子\2025\9月份绩效\9月 任务\1 postman 调试MES

#  让字符串中有语义的字符失去语义
s = r'F:\联昊电子\2025\9月份绩效\9月 任务\1 postman 调试MES'
print(s)  # F:\联昊电子\2025\9月份绩效\9月 任务\1 postman 调试MES

# 编码和解码
s = 'hello 中国'
#  编码: encode() 将 字符串 => 二进制
b1 = s.encode()  # utf-8 gbk
print(b1)  # b'hello \xe4\xb8\xad\xe5\x9b\xbd' 默认使用utf-8

b2 = s.encode('gbk')  # utf-8 gbk 不同的编码不一样
print(b2)  # b'hello \xd6\xd0\xb9\xfa'

b3 = s.encode('utf-8')  # utf-8 gbk
print(b3)  # b'hello \xe4\xb8\xad\xe5\x9b\xbd'

#  解码: decode() 将 二进制 => 字符串
c2 = b2.decode("gbk")
print(c2)  # hello 中国

c3 = b3.decode("utf-8")
print(c3)  # hello 中国

# ASCII码
print(ord('a'))  # 97 字母得到编码
print(chr(65))  # A

# strip() : 去除两边的指定字符(默认去除空格)
print("  nihao  ".strip()) #nihao
print("----ni---hao---".strip("-")) #ni---hao
print("----ni---hao---".lstrip("-")) #ni---hao---
print("----ni---hao---".rstrip("-")) #----ni---hao 去掉右边的-

# 对齐方式 : 了解
print('hello'.center(40)) # 居中 在宽度40的长度居中                  hello
print('hello'.ljust(40)) # hello
print('hello'.rjust(40)) #                                      hello
print('hello'.zfill(40)) # 00000000000000000000000000000000000hello

# 前缀 后缀 判断
print("helloword".startswith("hello"))
print("helloword".endswith("word"))