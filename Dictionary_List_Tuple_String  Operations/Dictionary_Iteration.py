xiaoming_dic = {"name": "小明",
                "age": "18",
                "height": "185",
                "weight": "155"}
# 在迭代遍历中 info获取的是键值对的key

for info in xiaoming_dic:
    print("%s: %s" % (info, xiaoming_dic[info]))