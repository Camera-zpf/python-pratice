xiaoming_dic = {"name": "小明",
                "age": "18"}

# 1.统计字典键值对的个数
print(len(xiaoming_dic))

# 2.合并两个字典
temp_dic = {"height": "185",
            "age": "20"}    # 如果加入已存在的键值对，则会覆盖
xiaoming_dic.update(temp_dic)
print(xiaoming_dic)
# 3.清空字典
xiaoming_dic.clear()
print(xiaoming_dic)

