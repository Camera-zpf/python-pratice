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
        # 1.针对子类特有的需求，编写代码
        print("神一样的叫唤。。。")
        # 2.使用super(). 方法调用原本在父类中封装的方法
        # super().bark()
        # 父类.方法名(self)
        # Dog.bark(self)

        # 注意：如果使用子类调用方法，会出现递归调用 --会出现死循环
        # Xiaotianquan.bark(self)
        # 3.增加其他子类的代码
        print("#%#%$&%")

xtq = Xiaotianquan()

xtq.fly()
# 如果在子类中，重写了父类的方法
# 则在调用方法时，会调用子类重写的方法
xtq.bark()