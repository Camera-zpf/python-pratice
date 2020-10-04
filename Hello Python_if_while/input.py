#超市买苹果
#1.输入苹果的价格
price = float(input("请输入苹果的单价："))

#2.输入买的重量
weight = float(input("请输入苹果的单价："))
#3.输出总金额
money = price * weight
print("您购买了%.02f斤苹果，苹果单价为%.02f，共需%%支付%.02f元" % (weight,price,money))