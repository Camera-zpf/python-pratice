def test(num):
    print("在函数内部 %d 对应的内存的是 %d" % (num, id(num)))
    # 1>定义一个字符串变量
    result = "hello"
    print("函数返回的变量的地址是 %d " % id(result))
    # 2>将字符串变量返回, 返回的是数据的引用，而不是数据本身
    return result

a = 10
# 数据的本质就是一个数字
print("a变量的地址是 %d " % id(a))
# 调用test函数，本质上是调用实参的引用，而不是实参保存的数据
# 注意函数有返回值，没有接受返回值，程序不会报错
r = test(a)
print("%s 字符串的内存地址是 %d " % (r, id(r)))
