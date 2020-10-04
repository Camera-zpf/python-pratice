class Cat:

    def __init__(self, new_name):
        """
        这是一个初始化方法
        """
        self.name = new_name
        print(" %s 来了" % self.name)

    def __del__(self):
        print(" %s 去了" % self.name)

    def __str__(self):
        # 必须返回一个字符串
        return "我是小猫[%s]" % self.name
# 在使用类名（）创建对象时，会自动调用初始化方法__init__
tom = Cat("Tom")
print(tom)