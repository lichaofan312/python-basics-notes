# 对列表进行降序排序(不修改原列表)
def sort1(l) -> list:
    return sorted(l, reverse=True)


# 对列表进行升序排序(不修改原列表):
def sort2(l) -> list:
    return sorted(l)


# 获取列表中所有与指定元素重复的元素下标，并返回这些下标所组成的列表
def find_index(l, n) -> list:
    # indexs = []
    # for i, val in enumerate(l):
    #     if val == n:
    #         indexs.append(i)
    # return indexs
    return [i for i, val in enumerate(l) if val == n]


#  1 如果在当前文件执行， 则 __name__ : __main__
#  2 在其他地方导入当前模块后，在其他地方执行， __name__ : 当前模块名 【test.sort】
print('__name__:', __name__)  # 模块名称 __main__： test.sort

#  1 作为文件入口， main() 代码开始执行的地方
#  2 作为测试用， 当前模块的测试代码
if __name__ == '__main__':  # 表示在当前文件执行
    ret = sort1([1, 2, 3, 5, 1, 3])  # 在当前文件中执行，
    print(ret)
