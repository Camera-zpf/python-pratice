import matplotlib.pyplot as plt
import numpy as np

# 从-1 到 1 平分 50 个点
x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2
plt.figure()
plt.plot(x, y1)

plt.figure(num=3, figsize=(10, 5))


plt.xlim((-1, 2))
plt.ylim((-2, 3))
plt.xlabel('I am X')
plt.ylabel('I am Y')

# linespace 将 -1 到 2 等分为五个单位
new_ticks = np.linspace(-1, 2, 5)
print(new_ticks)
plt.xticks(new_ticks)

plt.yticks([-2, -1.8, -1, 1.22, 3, ],
           [r'$really\ bad$', r'$bad\ \alpha$', r'$normal$', r'$good$', r'$really good$'])

# gca = 'get current axis'
ax = plt.gca()  # 获取当前的坐标轴
ax.spines['right'].set_color('none')  # 将右侧的坐标的颜色隐藏
ax.spines['top'].set_color('none')  # 将上方的坐标轴颜色隐藏
ax.xaxis.set_ticks_position('bottom')  # 将x轴设置为底部的坐标轴
ax.yaxis.set_ticks_position('left')  # 将y轴设置为左边的坐标轴
ax.spines['bottom'].set_position(('data', 0))  # 将x轴的位置放在y轴的数据‘0’的位置上
ax.spines['left'].set_position(('data', 0))  # 将y轴的位置放在x轴的数据‘0’的位置上
#

# 对线条标上标签
l1, = plt.plot(x, y2, label='up')
l2, = plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--', label='down')
plt.legend(handles=[l1,],labels=['aaa',], loc='best')
# plt.legend(handles=[l1,l2,],labels=['aaa', 'bbb'], loc='best') # handles表示需要显示label的个数

plt.show()
