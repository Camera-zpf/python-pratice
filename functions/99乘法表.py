def multiple_table():
    """打印九九乘法表"""
    i_row = 1
    while i_row <= 9:
        i_col = 1
        while i_col <= i_row:
            print("%d * %d = %d" % (i_col, i_row, i_col * i_row), end="\t")
            i_col += 1
        print("")
        i_row += 1


multiple_table()
