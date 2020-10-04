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


dog1 = Dog()
dog1.eat()
dog1.run()
dog1.sleep()
dog1.bark()
dog1.drink()
