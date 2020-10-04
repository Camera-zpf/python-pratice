def print_info(name, gender=True):
    """
    缺省参数在定义时必须处于末尾，当有多个缺省参数时，修改应该写出缺省参数的具体形参名   
    :param name:姓名：由用户输入
    :param gender:True是男生，False是女生
    :return:
    """
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("%s 是 %s" % (name, gender_text))


print_info("小明", True)
print_info("老王")
print_info("小美", False)
