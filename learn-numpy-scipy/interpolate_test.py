#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = 'tongzi'

import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

#要插值的数据
x = np.linspace(0, 10 * np.pi, 20)
y = np.cos(x)


#插值
f1 = interp1d(x, y, kind='linear')  #线性插值
fq = interp1d(x, y, kind='quadratic')  #二次插值

#x.min()和x.max()用于确保数据不会超出插值的边界
xint = np.linspace(x.min(), x.max(), 1000)

yintl = f1(xint)
yintq = fq(xint)

plt.plot(xint, yintl, xint, yintq)

plt.grid()
plt.legend(['Linear interpolate', 'Quadratic interpolate'])
plt.show()