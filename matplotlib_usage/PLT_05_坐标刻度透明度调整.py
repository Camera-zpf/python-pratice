import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y = 0.1 * x
plt.figure(num=3, figsize=(8,5))
plt.plot(x, y, linewidth=10,zorder=1)
plt.ylim(-2, 2)


ax = plt.gca()  # 获取当前的坐标轴
ax.spines['right'].set_color('none')  # 将右侧的坐标的颜色隐藏
ax.spines['top'].set_color('none')  # 将上方的坐标轴颜色隐藏
ax.xaxis.set_ticks_position('bottom')  # 将x轴设置为底部的坐标轴
ax.yaxis.set_ticks_position('left')  # 将y轴设置为左边的坐标轴
ax.spines['bottom'].set_position(('data', 0))  # 将x轴的位置放在y轴的数据‘0’的位置上
ax.spines['left'].set_position(('data', 0))  # 将y轴的位置放在x轴的数据‘0’的位置上


# begin
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='w', edgecolor='None', alpha=0))  # 此处不一定能显示，需要在plot中添加参数zorder=1

plt.show()
