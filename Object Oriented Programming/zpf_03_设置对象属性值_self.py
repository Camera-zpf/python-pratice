class Cat:
    def eat(self):
        # 哪一个对象调用的方法，self就是那个对象的引用
        print(" %s 爱吃鱼" % self.name)

    def drink(self):
        print(" %s 要喝水" % self.name)


# 创建猫对象

tom = Cat()

# 直接使用赋值语句对对象的属性设值，不推荐使用
tom.name = "Tom"
tom.eat()
tom.drink()

print(tom)

# 在创建一个猫对象
lazy_cat = Cat()

lazy_cat.name = "大懒猫"
lazy_cat.eat()
lazy_cat.drink()

print(lazy_cat)

lazy_cat2 = lazy_cat    # 引用，地址相同
print(lazy_cat2)
