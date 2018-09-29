#!/usr/bin/env python3
#-*- coding:utf-8 -*- 

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x = np.linspace(0, 2, 100)

#第一次调用plt.plot()自动创建一幅图像和相关的坐标，用于绘制图形
#后续再调用plt.plot()时将复用第一次创建的坐标轴并向图片中添加
#其它图形（直线、曲线等），前面设置的标题、图例说明和坐标轴名也
#会得到复用
plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')

plt.xlabel('x') #X Axis' name
plt.ylabel('y') #Y Axis' name

#the title of the figure
plt.title('Simple plot')
plt.legend() #
plt.show()

#Another plot test
x = np.arange(0, 10, 0.2)
y = np.sin(x)


fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()