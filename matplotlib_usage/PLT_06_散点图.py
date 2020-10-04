import matplotlib.pyplot as plt
import numpy as np
"""
生成散点图
"""
n = 1024
X = np.random.normal(0, 1, n)   # 生成随机数，平均值是0，方差是 1，一共生成n个数
Y = np.random.normal(0, 1, n)
T = np.arctan2(Y ,X)    # for color value

plt.scatter(X, Y, s=75, c=T, alpha=0.5)

plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
# plt.scatter(np.arange(5),np.arange(5))  # 生成5个点，一条直线
plt.xticks(())
plt.yticks(())
plt.show()