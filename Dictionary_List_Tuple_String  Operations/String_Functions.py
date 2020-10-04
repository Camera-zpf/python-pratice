str1 = "hello,hello"
# 1.统计字符串长度
print(len(str1))
# 2.统计某一个小字符串出现的次数
print(str1.count("llo"))
print(str1.count("abc"))
# 3.某一个字符串出现的位置
print(str1.index("llo"))
# print(str1.index("abc")) # 会报错 ValueError: substring not found
# 4. 字符串的操作函数很多，根据需求并ctrl+Q查看文档并灵活运用