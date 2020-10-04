class Cat:
    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫要喝水")


# 创建猫对象

tom = Cat()
tom.eat()
tom.drink()

print(tom)

addr = id(tom)  # 获取tom对象的地址
print("%x" % addr)  # 以十六进制输出地址
print("%d" % addr)  # 以十进制输出地址
