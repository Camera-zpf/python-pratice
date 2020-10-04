# 全局变量
gl_num = 10

def demo1():
    # 希望修改变量的值
    # 在python中不允许直接修改全局变量
    # 如果使用赋值语句，会在函数内部定义一个局部变量
    num = 99
    print("demo1函数内部的函数num是%d" % num)

def demo2():
    print("demo2函数内部的函数num是%d" % gl_num)

demo1()
demo2()