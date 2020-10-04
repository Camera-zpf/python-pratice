# 在每行打印*,依次递增
# *
# **
# ***
# ****
# *****


row = 1
while row <= 5:

    # 每一行打印的星星和行数是一样的
    # 增加一个循环,处理每一列的小星星
    col = 1
    while col <= row:
        print("*", end="")
        col += 1
    print("")

    row += 1