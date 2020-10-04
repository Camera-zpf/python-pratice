poem = "\t\n登鹳雀楼\t王焕之\t白日依山尽\t\n\t黄河入海流\t欲穷千里目\t更上一层楼"
print(poem)

# 要求：
# 1.将字符串的空白字符全部去除
# 2.再使用"  "分割符，拼接成一个整齐的字符串

# 1.拆分字符串
poem_list = poem.split()
print(poem_list)
# 2.合并字符串
result = " ".join(poem_list)
print(result)