# 列表的功能：对列表中元素操作
#    增删改查

# 增加: 添加元素
#    append(n) : 在列表的末尾追加元素
#    insert(i, n) : 在下标i的位置插入元素n
#    extend(iterable) : 在列表末尾添加多个元素
#           iterable:列表/元组/字符串/字典/集合
# 注意append和extend区别
nums = [1, 2, 3]
nums.append(4)
print(nums)  # [1, 2, 3, 4]
nums.insert(0, 4)
print(nums)  # [4, 1, 2, 3, 4]
nums.extend([90, 20])
print(nums)  # [4, 1, 2, 3, 4, 90, 20] 区别
nums.append([11, 22])
print(nums)  # [4, 1, 2, 3, 4, 90, 20, [11, 22]] 区别
print()
# 删除:
#    pop(i) : 弹出(删除并返回)下标i对应的元素, 默认删除最后一个元素
#    remove(n) : 删除指定元素n
#    clear() : 清空列表
nums = [10, 20, 30, 40, 50]
num = nums.pop()
print(num, nums)  # 50 [10, 20, 30, 40]
num = nums.pop(3)
print(num, nums)  # 40 [10, 20, 30]

nums = [11, 22, 33, 44, 55, 11]
# nums.remove(11)
# print(nums) # [22, 33, 44, 55, 11]
# count(): 计数,统计列表中元素出现的次数
while nums.count(11):
    nums.remove(11)
print(nums)  # [22, 33, 44, 55]

# clear() : 了解
nums.clear()
print(nums)  # []
print()

# 改: 修改元素
nums = [1, 2, 3]
nums[1] = 222
print(nums)  # [1, 222, 3]
# 查: 查询
#  索引: nums[1]
#  切片: nums[2:4]
#  循环: for n in nums:
#       for i in range():
#       for i,n in enumerate(nums):


# index(n) : 获取元素n第一次出现的下标,如果元素不存在则报错
nums = [2, 3, 3, 3, 4, 4, 5]
print(nums.index(3))  # 1
# print(nums.index(30)) # 30 is not in list error:

# 排序
#   sort() : 默认升序排列, 直接修改原列表
##     sorted(): 默认升序排列, 不改变原列表 (了解)
#   reverse() : 倒序,逆序, 直接修改原列表
##     reversed() : 倒序,逆序, 不改变原列表 (了解)
nums = [2, 4, 2, 6, 2, 6, 4, 6, 7, 8, 9, 222]
nums.sort()
print(nums) # [2, 2, 2, 4, 4, 6, 6, 6, 7, 8, 9, 222]
nums.sort(reverse=True)
# nums.reverse()
print(nums) # [222, 9, 8, 7, 6, 6, 6, 4, 4, 2, 2, 2]
print(nums[::-1]) # 切片不修改原列表 [2, 2, 2, 4, 4, 6, 6, 6, 7, 8, 9, 222]

nums = [2, 4, 2, 6, 2, 6, 4, 6, 7, 8, 9, 222]
nums2 = sorted(nums)
print(nums) # [2, 4, 2, 6, 2, 6, 4, 6, 7, 8, 9, 222]
print(nums2) # [2, 2, 2, 4, 4, 6, 6, 6, 7, 8, 9, 222] 升序
print()
nums1 = [2, 4, 2, 6, 2, 6, 4, 6, 7, 8, 9, 222]
nums3 = reversed(nums1)
print(nums1) # [2, 4, 2, 6, 2, 6, 4, 6, 7, 8, 9, 222]
print(nums3) # <list_reverseiterator object at 0x00000242018FFFA0>
print(list(nums3)) # [222, 9, 8, 7, 6, 4, 6, 2, 6, 2, 4, 2]

# copy(): 复制,拷贝
nums= [1,2,3]
nums2 = nums
nums[0] = 666
print(nums) # [666, 2, 3]
print(nums2) # [666, 2, 3]
print()
nums= [1,2,3]
nums2 = nums.copy() # 保留原来数据
nums[0] = 666
print(nums) # [666, 2, 3]
print(nums2) # [1, 2, 3]