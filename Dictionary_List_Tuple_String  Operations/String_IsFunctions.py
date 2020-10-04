# 1.判断空白字符
space_str = " \t\n\r"
print(space_str.isspace())
# 2.判断字符串是否只包含数字
# 1> 都不能判断小数
# num_str = "1.1"
# 2>Unicode字符串
# num_str = "\u00b2"
# 3> 中文数字
num_str = "一千零一"
# num_str = "1"
print(num_str.isdecimal()) # 不能判断 unicode字符     #  |
print(num_str.isdigit())                            #  |
print(num_str.isnumeric()) # 可以判断中文数字          #  ⬇ 依次增强判断范围


# 3.
# 4.
# 5.