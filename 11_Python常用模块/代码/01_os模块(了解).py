import os

# os  用于获取系统的功能，主要用于操作文件或者文件夹

print(os.name)  # nt 表示window操作系统
print(os.getcwd())  # 当前目录

# 创建目录: mkdir()  如果文件存在会报错
if not os.path.exists("hello"):
    os.mkdir('hello')  # 当文件已存在时，无法创建该文件。: 'hello'

# 创建多层目录: makedirs('a/b/c')
# os.makedirs('a/b/c')

# 删除空目录: rmdir
# os.rmdir('hello')

# 删除文件: remove
# os.remove('test.py')

# 重命名: rename
# os.rename('hello','hello2')

# listdir() : 返回指定目录下的所有文件或文件夹名组成的列表
dir_list = os.listdir(r'D:\Users\Administrator\Desktop\pythonLib\pythonDemo_AGI\11_Python常用模块\代码')
print(dir_list)

# os.path
#  os.path.exists : 文件或文件夹是否存在
#  os.path.isfile() : 是否为文件
# os.path.isdir() : 是否为目录

# 判断路径是否存在
print(os.path.exists(r'D:\Users\Administrator\Desktop\pythonLib\pythonDemo_AGI'))
# 判断是否是文件夹
print(os.path.isdir(r'D:\Users\Administrator\Desktop\pythonLib\pythonDemo_AGI'))
print(os.path.isfile(
    r'D:\Users\Administrator\Desktop\pythonLib\pythonDemo_AGI\11_Python常用模块\代码\01_os模块(了解).py'))
# 合并路径
print('合并路径: ', os.path.join(r'D:\Users\Administrator\Desktop\pythonLib\pythonDemo_AGI', 'a.py'))
# 需求: 将指定目录下的子目录的绝对路径打印
root_dir = r'D:\Users\Administrator\Desktop\pythonLib\pythonDemo_AGI\11_Python常用模块\代码'
print(os.listdir(root_dir))
for path in os.listdir(root_dir):
    subPath = os.path.join(root_dir, path)
    if os.path.isdir(subPath):
        print(subPath)

# 绝对路径: 从盘符开始的路径
# 相对路径: 从当前文件所在目录开始的路径

# os.path.split : 拆分 文件路径拆分
print(os.path.split(r"D:\Users\Administrator\Desktop\pythonLib\pythonDemo_AGI\11_Python常用模块\代码\hello"))

# os.path.splittext() : 拆分文件的扩展名
print(os.path.splitext(r'04_文件操作.py')) # ('04_文件操作', '.py')

# 文件大小:字节
print(os.path.getsize('01_os模块(了解).py')) # 2195
# 绝对路径 存在
print(os.path.abspath(r'04_文件操作.py'))