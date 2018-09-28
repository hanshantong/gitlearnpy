#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = 'tongzi'

import numpy as np
from scipy.integrate import quad, trapz
import matplotlib.pyplot as plt

#排序：np.sort()； np.clip(a_min, a_max):限制数据的范围
x = np.sort(np.random.randn(150) * 4 + 4).clip(0, 5)

func = lambda x: np.sin(x) * np.cos(x **2) + 1
y=func(x)

#积分
fsolution = quad(func, 0, 5)
dsolution = trapz(y, x=x)

print('fsolution = ' + str(fsolution[0]))
print('dsolution = ' + str(dsolution))

print('The defference is ' + str(np.abs(fsolution[0] - dsolution)))


'''
输出：
fsolution = 5.100345067540932
dsolution = 5.130291463293363
The defference is 0.02994639575243152

结论：quad只能对应函数进行积分， 而trapz可以对离散数据点进行积分
'''


#绘图

xint = np.linspace(0, 6, 1000)
yint = func(xint)

plt.plot(xint, yint)
plt.scatter(x, y)

plt.grid()
plt.show()


