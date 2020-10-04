Student = [
    {"name": "小明",
                "age": "18",
                "height": "185",
                "weight": "155"},
    {"name": "小小明",
                "age": "15",
                "height": "165",
                "weight": "105"},
    {"name": "大明",
                "age": "28",
                "height": "185",
                "weight": "195"}
]
find_name = "小小明"

for str_student in Student:
    # print(str_student)
    if str_student["name"] == find_name:
        print("找到了 %s " % find_name)
        break
    else:
        print("抱歉，没有找到 %s " % find_name)
# for循环的else在循环结束后还没有找到所需要的目标
# 希望得到一个统一的提示
# else:
#     print("抱歉，没有找到 %s " % find_name)

print("循环结束")