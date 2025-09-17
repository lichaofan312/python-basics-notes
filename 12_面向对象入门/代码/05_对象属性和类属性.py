class Person:
    # 类属性
    sex = "男"
    age = 30

    def __init__(self, name, age):
        self.name = name  # 对象属性
        self.age = age


# 对象属性的调用： 对象来调用
p = Person('小黄', 10)
"""
print(p.name)
# type object 'Person' has no attribute 'name' 不可以用类名来调用对象属性
# print(Person.name)

# 类属性调用 建议用类名来调用
print(p.sex)
print(Person.sex)
"""
#  对age 操作 即使类也是对象属性
print(p.age)  # 10 # 优化获取对象属性， 如果对象属性没有赋值， 可以获取类属性
print(Person.age)  # 30

print("*" * 100)
# 修改
Person.age = 40
print(Person.age)  # 40

p.age = 13 # 这种写法， 不管有没有对象属性age, 都不会修改类属性age, 新增了对象属性age
print(p.age)  # 13
print(Person.age)  # 40

# 总结
#  尽量用对象去操作对象属性
#  尽量用类去操作类属性

# 扩展
# 同一个类的类属性， 可以被这个类创建的不同对象共享的 针对可变类型， list
class Dog:
    likes = ['骨头']
    def __init__(self,name):
        self.name = name
        self.likes2 = ['骨头']

dog1 = Dog('小红')
dog2 = Dog('小黄')
#  修改类属性
Dog.likes.append('肉')
print(dog1.likes) # ['骨头', '肉']
print(dog2.likes) # ['骨头', '肉']

dog1.likes2.append("肉1")
dog2.likes2.append("肉2")
print(dog1.likes2) # ['骨头', '肉1'] 对象属性是： dog1 独有的
print(dog2.likes2) # ['骨头', '肉2']