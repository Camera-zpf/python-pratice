card_list = []


def show_menu():
    """显示菜单"""
    print("*" * 50)
    print("欢迎使用【名片管理系统】 V 1.0")
    print("")
    print("1.新增名片\t2.显示全部\t\n3.搜索名片\t0.退出系统")
    print("*" * 50)


def new_card():
    """新增名片"""
    print("-" * 50)
    print("新增名片:")
    # 1.提示用户输入信息
    name_str = input("请输入姓名:")
    phone_str = input("请输入电话:")
    qq_str = input("请输入qq号:")
    email_str = input("请输入邮箱:")
    # 2.将用户输入的信息添加到名片字典中
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str}
    # 3.将字典添加到名片列表中
    card_list.append(card_dict)
    # 4.提示用户添加成功
    print(card_list)
    print("添加 %s 的名片成功!" % name_str)


def show_card():
    """显示名片"""
    print("-" * 50)
    print("显示所有名片:")
    if len(card_list) == 0:
        print("当前还没有添加任何名片，请使用名片添加功能添加名片")
        return
    print("-" * 50)
    # 打印表头
    for name in ["姓名", "电话", "qq", "邮箱"]:
        print(name, end="\t\t")
    print("")
    # 打印分割线

    print("=" * 50)
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))


def search_card():
    """搜索名片"""
    print("-" * 50)
    print("搜索名片:")
    search_str = input("请输入需要查询的姓名：")
    for card_dict in card_list:
        if card_dict["name"] == search_str:
            print("查询 %s 成功！")
            for name in ["姓名", "电话", "qq", "邮箱"]:
                print(name, end="\t\t\t")
            print("")
            print("=" * 50)
            print("%s\t\t\t%s\t\t%s\t\t%s\t" % (card_dict["name"],
                                                card_dict["phone"],
                                                card_dict["qq"],
                                                card_dict["email"]))
            deal_card(card_dict)
            break
    else:
        print("查找失败")


def deal_card(find_dict):
    """
    处理找到的名片
    :param find_dict: 查找的名片
    :return:
    """
    print(find_dict)
    action_str = input("请输入要执行的操作 1.修改  2.删除  3.返回上一级")
    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"], "姓名：")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话：")
        find_dict["qq"] = input_card_info(find_dict["qq"], "qq；")
        find_dict["email"] = input_card_info(find_dict["email"], "邮箱：")

        print("修改名片成功！")
    elif action_str == "2":
        card_list.remove(find_dict)
        print("删除名片成功！")


def input_card_info(dict_value, tip_message):
    """
    对input函数的加强版，可输入或不输入值，不输入返回原有值，输入返回输入的值
    :param dict_value: 原字典中的值
    :param tip_message: 提示用户输入信息
    :return: 返回用户输入的值
    """
    # 1.提示用户输入内容
    result_str = input(tip_message)
    # 2.针对用户输入进行判断，如果用户输入了内容则直接返回，没有输入则返回原有的值
    if len(result_str) > 0:
        return result_str
    else:
        return dict_value
