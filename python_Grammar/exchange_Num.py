a = 10
b = 20
# 1> 使用其他变量
print("a:%d  b:%d" % (a, b))
c = a
a = b
b = c
print("交换后输出")
print("a:%d  b:%d" % (a, b))
# 2> 不使用其他变量
a = a + b
b = a - b
a = a - b
print("交换后输出")
print("a:%d  b:%d" % (a, b))
# 3> python专有
# a, b = (b, a)
a, b = b, a # 等号右边是一个元祖，只是把括号省略了
print("交换后输出")
print("a:%d  b:%d" % (a, b))