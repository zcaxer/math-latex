# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

frequency = np.array([0.15, 0.20, 0.30, 0.20, 0.10, 0.05])
bin_edge = np.array([1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5])
x_label = u"百分比"
y_label = u"频率/组距"
title = u'甲离子残留百分比直方图'

def ddot(ax, x, value):
        '''画水平虚线
        ax:axes
        x:x最大值，决定虚线长度
        value:虚线高度'''
        ax.hlines(y=value, xmin=0, xmax=x, linewidth=1, color='k', linestyles='--')


fig, ax = plt.subplots()
ax.set_title(title, y=-0.15)

ax.set_xlim(bin_edge[0] - 0.3, bin_edge[-1] + 0.3)
y_tick = np.unique(frequency)
y_tick.sort()
ax.set_xlabel(x_label)
ax.set_ylabel(y_label, rotation=0)
ax.set_xticks(bin_edge)
ax.set_yticks(y_tick)
ax.xaxis.set_label_coords(1.03, -0.02)  # x轴标签位置
ax.yaxis.set_label_coords(0.08, 1)  # y轴标签位置
ax.hist(bin_edge[:-1], bin_edge, density=1,
        weights=frequency, linewidth=0.5, edgecolor='k', color='w')

ax.spines['right'].set_visible(False)  # 获取绘图区的轴对象（spines），设置右边框不显示
ax.spines['top'].set_visible(False)  # 获取绘图区的轴对象（spines），设置上边框不显示

ax.arrow(0, -0.001, bin_edge[-1] + 0.16, 0, width=0.0000001,
         head_width=0.012, head_length=0.14, fc='k', ec='k')
ax.arrow(1.19999, 0, 0, y_tick[-1] + 0.002, width=0.0000001,
         head_width=0.15, head_length=0.015, fc='k', ec='k')

i = 0
while i < len(bin_edge) - 1:
    ddot(ax, bin_edge[i], frequency[i])
    i += 1

plt.tight_layout()
plt.show()

