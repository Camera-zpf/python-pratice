class Cat:

    def __init__(self, new_name):
        """
        这是一个初始化方法
        """
        self.name = new_name
        print("这是一个初始化方法")
    def eat(self):
        print(" %s 爱吃鱼" % self.name)

# 在使用类名（）创建对象时，会自动调用初始化方法__init__
tom = Cat("Tom")
tom.eat()

lazy_cat = Cat("大懒猫")
lazy_cat.eat()