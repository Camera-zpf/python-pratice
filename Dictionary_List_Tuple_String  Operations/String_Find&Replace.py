
hello_str = "hello hello"
# 1.判断是否以指定字符转开始
print(hello_str.startswith("hel"))
print(hello_str.startswith("abc"))
# 2.判断是否以指定的字符串结束
print(hello_str.endswith("llo"))
print(hello_str.endswith("abc"))
# 3.查找指定字符串
print(hello_str.find("llo"))
# 4.替换字符串
new_str = hello_str.replace("ello", "i")
print(new_str)