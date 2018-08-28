#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = 'tongzi'

import numpy as np
from scipy.interpolate import SmoothBivariateSpline as SBS
import matplotlib.pyplot as plt


#定义一个波纹函数
ripple = lambda x, y:np.sqrt(x**2 + y**2) + np.sin(x**2 + y**2)

#采样数据，用于插值
xy = np.random.rand(1000, 2)
x, y = xy[:,0],xy[:,1]
sample = ripple(xy[:,0] * 5, xy[:,1] * 5)

#插值
fit = SBS(x * 5, y * 5, sample, s=0.01, kx=4, ky=4)
interp = fit(np.linspace(0, 5, 1000), np.linspace(0, 5, 1000))
plt.imshow(interp)

plt.show()