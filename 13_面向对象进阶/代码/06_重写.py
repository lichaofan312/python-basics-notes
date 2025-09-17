# 重写: 方法重写，在继承的基础上，子类和父类有一样的方法名称。
class Person:
    def run(self):
        print('person 父类中 Run')


class Boy(Person):
    # 方法的重写  优先调用子类的run
    def run(self):
        print('子类中的run')


boy = Boy()
boy.run()
p = Person()
p.run()
