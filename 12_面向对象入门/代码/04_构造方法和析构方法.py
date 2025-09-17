# __init__ 创建对象时自动调用
# __del__  销毁对象时 自动调用
import time


class Animal:
    def __init__(self, name):
        self.name = name
        print("构造方法 创建对象时自动调用")

    def __del__(self):
        #  在这里可以写手动是否需要释放内存的操作 关闭文件
        print("析构方法 销毁对象时 自动调用")


cat = Animal('咪咪')

time.sleep(2)
del cat # 手动删除
time.sleep(3)
print('end')
