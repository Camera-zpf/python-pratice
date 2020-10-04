poem =["\t\n登鹳雀楼",
       "王焕之",
       "白日依山尽\t\n",
       "黄河入海流",
       "欲穷千里目",
       "更上一层楼"]
for poem_str in poem:
    # print("|%s|" % poem_str.rjust(10, " "))
    #       假设上述内容是从网上抓取的，要求居中对齐输出上述内容
    # 先使用strip方法去除字符串中的空白字符
    # 再使用center方法居中显示文本
    print("|%s|" % poem_str.strip().center(10, " "))
