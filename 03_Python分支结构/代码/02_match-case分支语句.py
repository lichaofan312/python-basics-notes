
# 输入您的等级，输出对应的成绩范围
#    A ：  >= 90
#    B ：70 ~ 90
#    C : 60 ~ 70
#    D :  < 60

# match-case : Python3.10及以上版本
# 了解
n = input("输入(A/B/C/D): ")
match n:
    case 'A':
        print(">=90")
    case 'B':
        print("70 ~ 90")
    case 'C':
        print("60 ~ 70")
    case 'D':
        print("< 60")



