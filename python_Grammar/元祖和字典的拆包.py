def demo(*args, **kwargs):
    print(args)
    print(kwargs)

# 元祖变量/字典变量
gl_nums = (1, 2, 3)
gl_dict = {"name":"xiaoming",
           "age": 18}
# demo(gl_nums,gl_dict)
# 拆包语法，简化元祖变量/字典变量的传递
demo(*gl_nums, **gl_dict)

demo(1, 2, 3, name="xiaoming",age=18)