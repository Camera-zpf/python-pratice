def sum_num(num):
    if num == 0:
        return 1


    temp = sum_num(num - 1)
    return num + temp

result = sum_num(5)
print(result)

