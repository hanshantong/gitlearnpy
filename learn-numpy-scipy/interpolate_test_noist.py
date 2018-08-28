#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = 'tongzi'

import numpy as np
from scipy.interpolate import UnivariateSpline
import matplotlib.pyplot as plt

#要插值的数据
sample = 30
x = np.linspace(1, 10 * np.pi, sample)
y = np.cos(x) + np.log10(x) + np.random.randn(sample) / 10

def func(x):
	return np.cos(x) + np.log10(x)

#插值
f = UnivariateSpline(x, y, s=1)  #s是平滑因子，若s=0，则插值曲线会忽略噪声，穿过所有的采样点


#x.min()和x.max()用于确保数据不会超出插值的边界
xint = np.linspace(x.min(), x.max(), 1000)

yint = f(xint)

y_true = func(xint)

plt.plot(xint, yint, xint, y_true)
plt.scatter(x,y)

plt.grid()
plt.legend(['Linear interpolate','True function value'])
plt.show()