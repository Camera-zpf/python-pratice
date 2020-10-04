# 导入随机包
import random
# 打印n次Hello World

i = 0  # 计数器
n = random.randint(1, 10)
while i < n:
    print("Hello World")
    # 处理计数器
    i += 1
print("循环结束,共打印了%d次" % n)