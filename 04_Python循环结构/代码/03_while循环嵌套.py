''' '''
# 打印下面的图形，要求一次只能打印一个"*"，写循环嵌套
# 3行5列
'''
*****
*****
*****
'''
row = 1
while row <= 3:
    column = 1
    while column <= 5:
        print("*", end="")
        column += 1
    print()
    row += 1

print()
# 打印下面图形，要求一次只能打印一个"*"
'''
*
**
***
****
*****
'''
NUM = 5
row = 1
column = 1
count = column
while row <= NUM:
    column = 1
    while column <= row:
        print("*", end="")
        column += 1
    print()
    row += 1

print()
# 打印一个等腰三角形, 要求一次只能打印一个"*"
'''          i   空格数量     *的数量
    *        1     4(=5-i)     1(=2*i-1)
   ***       2     3           3
  *****      3     2           5 
 *******     4     1           7
*********    5     0           9
'''

i = 1
NUM = 5
space = 1
star = 1
while i <= NUM:
    spaceCount = NUM - i
    starCount = 2 * i - 1
    while space <= spaceCount:
        print(" ", end="")
        space += 1
    while star <= starCount:
        print("*", end="")
        star += 1
    print()
    space = 1
    star = 1
    i += 1
