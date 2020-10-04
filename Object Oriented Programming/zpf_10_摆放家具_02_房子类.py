class HouseItem:

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地 %.2f" % (self.name, self.area)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        # 剩余面积
        self.free_are = area
        # 家具名称列表
        self.item_list = []

    def __str__(self):
        return "户型是 %s ,\n总面积 %.2f,安放家具有 %s\n 剩余面积 %.2f." % (self.house_type,
                                                             self.area, self.item_list, self.free_are)

    def add_item(self, item):
        print("要添加 %s " % item)
        # 判断家具的大小
        if item.area > self.free_are:
            print("%s 占地太大了，无法添加" % item.name)

            return
        self.free_are = self.free_are - item.area   # 每添加一件家具，计算剩余面积
        self.item_list.append(item.name)    # 将添加的家具添加到家具列表当中去


# 1.创建家具
bed = HouseItem("席梦思", 4.0)
chest = HouseItem("衣柜", 2.0)
table = HouseItem("餐桌", 1.5)

# print(table)
# print(bed)
# print(chest)

# 创建房子对象
my_house = House("两室一厅", 65)
my_house.add_item(bed)
my_house.add_item(table)
my_house.add_item(chest)

print(my_house)
