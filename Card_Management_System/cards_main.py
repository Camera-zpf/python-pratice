#! D:\pycharm workspace\Card_Management_System\venv\Scripts\python

import cards_tools
while True:
    cards_tools.show_menu()
    action_str = input("请选择希望执行的操作:")
    print("您所选的操作是【%s】" % action_str)

    # 1,2,3针对名片操作
    if  action_str in ["1", "2", "3"]:
        if action_str == "1":
            # 新增名片
            cards_tools.new_card()

        elif action_str == "2":
            # 显示全部
            cards_tools.show_card()
        elif action_str == "3":
            # 查询名片
            cards_tools.search_card()
    # 0退出系统
    elif action_str == "0":

        print("欢迎再次使用【名片管理系统】")
        break
    # 其他内容输入错误，需要提示用户
    else:
        print("您输入不正确，请重新输入！")