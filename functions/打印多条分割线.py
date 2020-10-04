def print_line(char, times):
    """
    打印单行分割线
    :param char: 分割字符
    :param times: 字符个数
    """
    print(char * times)


def print_lines(char, times, row):
    """
    打印多条分割线
    :param char: 分割线所用的字符
    :param times:分割线打印的个数
    :param row:分割线打印的行数
    """
    row1 = 0
    while row1 < row:
        print_line(char, times)
        row1 += 1

# print_lines("*", 50, 5)
