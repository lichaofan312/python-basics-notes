# 1. 已知列表list1 = ['mon','sun','sat','fri','thu','wed'],
#          list2 = ['sun','wed','thu']，将属于list2的元素从list1中删除
list1 = ['mon', 'sun', 'sat', 'fri', 'thu', 'wed']
list2 = ['sun', 'wed', 'thu']
list3 = []
for i, str1 in enumerate(list1):
    if str1 not in list2:
        list3.append(str1)
print(list1)

# 2. 已知一个列表names = ['鲁班七号', '后裔', '狄仁杰', '黄忠', '孙尚香']，
#    利用索引的方法获取names中的元素黄忠
names = ['鲁班七号', '后裔', '狄仁杰', '黄忠', '孙尚香']
for i in range(len(names)):
    if names[i] == '黄忠':
        print(i, names[i])
        break

# 3. 已知一个数字列表nums = [1, 2, 3, 1, 4, 2, 1, 3, 7, 3, 3]，输出索引为奇数的元素
nums = [1, 2, 3, 1, 4, 2, 1, 3, 7, 3, 3]
for i, num in enumerate(nums):
    if i % 2 != 0:
        print(f'索引:{i}, 元素：{num}')
