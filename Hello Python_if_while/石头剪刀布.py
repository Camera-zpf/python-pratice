# 导入随机工具包
import random
# 从控制台输入你要出的拳————石头(1)剪刀(2)布(3)
player = int(input("请输入你要输入的拳————石头(1)剪刀(2)布(3)："))

# 电脑随机出拳

computer = random.randint(1, 3)
print("玩家选择的拳是%d  -  电脑出的拳是%d" % (player, computer))

# 比较胜负
# 1石头胜剪刀
# 2剪刀胜布
# 3布胜石头
if (player == 1 and computer == 2) \
        or (player == 2 and computer == 3) \
        or (player == 3 and computer == 1):

    print("您胜出了")
elif player == computer:
    print("平局")
else:
    print("您输了")
