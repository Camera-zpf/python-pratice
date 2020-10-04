class Animal:
    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


# class 派生类（基类）:
class Dog(Animal):  # class 类名（父类名）:
    def bark(self):
        print("汪汪叫")


class Xiaotianquan(Dog):        # 继承的传递，子类拥有父类的方法和属性
    def fly(self):
        print("我会飞")

    def bark(self):
        print("我是哮天犬，喔喔")

xtq = Xiaotianquan()

xtq.fly()
# 如果在子类中，重写了父类的方法
# 则在调用方法时，会调用子类重写的方法
xtq.bark()