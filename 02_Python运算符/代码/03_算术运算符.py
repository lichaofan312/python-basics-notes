# Python算术运算符：
#    +  -  *  /  %  //（整除:向下取整）   **次方（取幂）
print(10 + 4)
print(10 - 4)
print(10 * 4)
print(10 / 4)  # 2.5
print(-10 / 4)  # -2.5
print(10 % 4)
print(10 // 4)  # （整除:向下取整） 2
print(-10 // 4)  # （整除:向下取整） -3
print(10 ** 4)

# 科学计数法
a = 3.14 * 10 ** 5
print(a)
b = 3.14e5
print(b)

# 常见内存单位：
# 1b = 0 或 1
# 1B = 8bit
# 1KB = 1024Byte
# 1MB = 1024KB
# 1GB = 1024MB
# 1TB = 1024GB
# 1PB = 1024TB
# 1EB = 1024PB
# ...

# 练习： 从控制台输入一个三位数， 取出个位， 十位，百位
n = int(input("origin: "))
# print(f"个位：{origin%10},  十位{int(origin/10%10)}，百位{int(origin/100)}")
a = n // 100  # 百位
b = n // 10 % 10  # 十位
c = n % 10
print(a, b, c)
