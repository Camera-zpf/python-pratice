def sum_nums(*args):
    sum = 0
    for num in args:
        sum += num
    print("sum = %d" % sum)


sum_nums(1, 2, 3, 4, 5)
