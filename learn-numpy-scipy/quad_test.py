#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = 'tongzi'

import numpy as np

from scipy.integrate import quad
import matplotlib.pyplot as plt



func = lambda x: np.cos(np.exp(x)) ** 2

#积分，积分区间:[0, 3]
solution = quad(func, 0, 3)

print(solution)

'''
输出：
(1.296467785724373, 1.397797133112089e-09)
第一个值是积分的结果， 第二个是积分的误差项

'''

#绘图
x = np.linspace(0, 4, 1000)
y = func(x)

plt.plot(x, y)

plt.grid()
plt.show()


