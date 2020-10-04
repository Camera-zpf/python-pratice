def measure():
    """测量温度和湿度"""
    print("开始测量温度....")
    temperature = 19
    print("开始测量湿度...")
    wetness = 20
    print("测量结束")
    # return (temperature, wetness)   # 返回元祖
    return temperature, wetness    # 返回元祖时，可以省略括号

# 1> 通过元祖接受返回的多个数据
# result = measure()
# print(type(result))
# print("当前温度为 %d ,湿度为 %d" % result)
# 2> 通过多个变量接受返回的元祖
# 注意：变量的个数需要和元祖的元素个数数量相同
gl_temperature, gl_wetness = measure()
print("当前温度为 %d ,湿度为 %d" % (gl_temperature, gl_wetness))