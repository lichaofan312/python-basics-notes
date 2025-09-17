# c.在另外一个文件中 aa.py导入上述包中的模块sort.py，完成模块中功能的调用
from test import sort

print(sort.sort1([2, 3, 4, 1, 2, 56, 2, 89, 1])) # [89, 56, 4, 3, 2, 2, 2, 1, 1]
print(sort.sort2([2, 3, 4, 1, 2, 56, 2, 89, 1])) # [1, 1, 2, 2, 2, 3, 4, 56, 89]
print(sort.find_index([2, 3, 4, 1, 2, 56, 2, 89, 1], 1)) # [3, 8]
