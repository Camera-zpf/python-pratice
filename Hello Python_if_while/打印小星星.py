# 在每行打印*,依次递增
# *
# **
# ***
# ****
# *****

row = 0

while row < 5:
    print("*" * (row + 1))

    row += 1