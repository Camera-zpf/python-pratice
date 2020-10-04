import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    """the height function:根据给定的(x,y)求出高度值"""
    return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)

n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)    # 将x,y绑定为网格值
# 0 表示分成两部分，8表示分成10部分
plt.contourf(X, Y, f(X, Y), 8, alpha=0.75, cmap=plt.cm.hot)   # 给等高线上色

C = plt.contour(X, Y, f(X, Y), 8, color='black', linewidth=.5)  # 画上等高线，并定义颜色，粗细等

plt.clabel(C, inline=True, fontsize=10) # 给等高线加上标签


plt.xticks(())
plt.yticks(())
plt.show()
