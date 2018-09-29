#!/usr/bin/env python3
#-*- coding:utf-8 -*- 

import matplotlib.pyplot as plt
import numpy as np

#Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

#设置坐标轴名，标题
ax.set(xlabel='time(s)', ylabel='voltage (mV)',
		title='About as simple as it gets, folks')
		
ax.grid()#网格
fig.savefig('simple_plot.png')#保存图片
plt.show()
