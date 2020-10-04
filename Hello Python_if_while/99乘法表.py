# 打印99乘法表

i_row = 1

while i_row <= 9:
    # 输出乘法表每一行
    i_col = 1
    while i_col <= i_row:
        print("%d * %d = %d " % (i_col, i_row, i_row * i_col), end="\t")
        i_col += 1
    print("")
    i_row += 1
