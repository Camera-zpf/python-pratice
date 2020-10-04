class Person:

    def __init__(self, name, weight):
        """初始化方法"""
        # self.属性 = 形参
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字是【%s】,体重是 %.2f 公斤" % (self.name, self.weight)

    def run(self):
        print(" %s 爱跑步，跑步锻炼身体！" % self.name)
        self.weight -= 0.5

    def eat(self):
        print(" %s 爱吃东西，吃完这顿再减肥" % self.name)
        self.weight += 1


# 新建一个小明对象
xiaoming = Person("小明", 75)
xiaoming.run()
xiaoming.eat()
xiaoming.run()
print(xiaoming)

# 新建一个小美对象
xiaomei = Person("小美", 45)
print(xiaomei)
xiaomei.eat()
xiaomei.eat()
print(xiaomei)
