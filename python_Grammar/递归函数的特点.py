def print_num(num):

    print(num)
    if num == 1:    # 递归的出口
        return
    print_num(num - 1)  # 自己调用自己

print_num(3)