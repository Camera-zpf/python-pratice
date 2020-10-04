XiaoMing = {"name": "小明"}

# 1.增加/修改
XiaoMing["age"] = 18
XiaoMing["name"] = "小小明"  # 如果key值存在，则修改已存在键值对
# 2.取值  如果kye 值不存在则程序会报错
print(XiaoMing["name"])
print(XiaoMing)
# 3.删除
XiaoMing.pop("name")
print(XiaoMing)
