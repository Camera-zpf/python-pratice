has_ticket = True

knife_length = 10

if has_ticket:
    print("请通过并进行安检！")
    if knife_length > 20:
        print("您的刀太长，%d超过安检标准" % knife_length)
    else:
        print("安检通过，祝您旅途愉快")
else:
    print("请先买票")