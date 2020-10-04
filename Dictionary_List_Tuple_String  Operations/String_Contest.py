poem =["登鹳雀楼",
       "王焕之",
       "白日依山尽",
       "黄河入海流",
       "欲穷千里目",
       "更上一层楼"]

for poem_str in poem:
    # print("|%s|" % poem_str.center(10, " "))
    # print("|%s|" % poem_str.ljust(10, " "))
    print("|%s|" % poem_str.rjust(10, " "))