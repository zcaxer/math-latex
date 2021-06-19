# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# plt.rcParams['text.usetex'] = True  # 使用latex排版系统
fig = plt.figure()

# 使用axisartist.Subplot方法创建一个绘图区对象ax
ax = axisartist.Subplot(fig, 111)
# 将绘图区对象添加到画布中
fig.add_axes(ax)
# 通过set_visible方法设置绘图区所有坐标轴隐藏
ax.axis[:].set_visible(False)

# ax.new_floating_axis代表添加新的坐标轴
ax.axis["x"] = ax.new_floating_axis(0, 0)
# 给x坐标轴加上箭头
ax.axis["x"].set_axisline_style("->", size=1.0)
# 添加y坐标轴，且加上箭头
ax.axis["y"] = ax.new_floating_axis(1, 1)
ax.axis["y"].set_axisline_style("->", size=1.0)
# 设置x、y轴上刻度显示方向
ax.axis["x"].set_axis_direction("top")
ax.axis["y"].set_axis_direction("right")

frequency = np.array([0.15, 0.20, 0.30, 0.20, 0.10, 0.05])
bin_edge = np.array([1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5])
ax.axis['x'].set_label(u"百分比")
ax.axis['y'].set_label(u"频率/组距")

x_tick = np.linspace(1.5, 7.5, 7)
ax.set_xticks(x_tick)
ax.set_yticks([0.05, 0.10, 0.15, 0.20, 0.30])
ax.hist(bin_edge[:-1], bin_edge, density=1,
        weights=frequency, linewidth=0.5, edgecolor='k', color='w')
# ax.axis['left'].set_axisline_style('->')  # 给y轴加一个箭头
# ax.axis['bottom'].set_axisline_style('->')  # 给x轴加一个箭头
# ax.spines['right'].set_visible(False)  # 获取绘图区的轴对象（spines），设置右边框不显示
# ax.spines['top'].set_visible(False)  # 获取绘图区的轴对象（spines），设置上边框不显示

plt.show()
