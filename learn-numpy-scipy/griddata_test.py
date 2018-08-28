#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = 'tongzi'

import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt


#定义一个波纹函数
ripple = lambda x, y:np.sqrt(x**2 + y**2) + np.sin(x**2 + y**2)

#生成网格数据

grid_x, grid_y = np.mgrid[0:5:1000j, 0:5:1000j]

#采样数据，用于插值
xy = np.random.rand(1000, 2)
sample = ripple(xy[:,0] * 5, xy[:,1] * 5)

#插值
grid_z0 = griddata(xy * 5, sample, (grid_x, grid_y), method='cubic')
print(type(grid_x))
plt.imshow(grid_z0)

plt.show()