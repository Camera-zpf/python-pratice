import matplotlib.pyplot as plt
import numpy as np

# 从-1 到 1 平分 50 个点
x = np.linspace(-3, 3, 50)
y = 2 * x + 1

plt.figure()
plt.plot(x, y)

ax = plt.gca()  # 获取当前的坐标轴
ax.spines['right'].set_color('none')  # 将右侧的坐标的颜色隐藏
ax.spines['top'].set_color('none')  # 将上方的坐标轴颜色隐藏
ax.xaxis.set_ticks_position('bottom')  # 将x轴设置为底部的坐标轴
ax.yaxis.set_ticks_position('left')  # 将y轴设置为左边的坐标轴
ax.spines['bottom'].set_position(('data', 0))  # 将x轴的位置放在y轴的数据‘0’的位置上
ax.spines['left'].set_position(('data', 0))  # 将y轴的位置放在x轴的数据‘0’的位置上

x0 = 1
y0 = 2 * x0 + 1
plt.scatter(x0, y0, s=50, color='b')  # scatter表示散点图，该语句代表显示(x0,y0)这个点,s代表size,color表示该点的颜色
plt.plot([x0, x0], [y0, 0], 'k--', lw=1.5)
plt.plot([x0, 0], [y0, y0], 'r--', lw = 1.5)

# method 1
plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30,-30),textcoords='offset points',
             fontsize=16,arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))

# method 2
plt.text(-3.7,3,r'$This\ is\ the\ some\ text.\ \mu\ \alpha_i\ \sigma_u$',fontdict={'size':12,'color':'r'})



plt.show()
