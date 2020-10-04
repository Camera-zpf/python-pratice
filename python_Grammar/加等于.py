def demo(num, num_list):
    print("函数开始")

    num += num
    # 列表变量加等于不是做相加在赋值的操作
    # num_list = num_list + num_list
    # 本质上是在做列表的 extend 方法
    num_list += num_list
    # num_list.extend(num_list)

    print(num_list)

    print(num)
    print("函数结束")

gl_list = [1, 2, 3, 4]
gl_num = 9
demo(gl_num, gl_list)
print(gl_num)
print(gl_list)