#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = 'tongzi'
'''
几何分布：PMF= p*（1-p）^(k-1)
'''


import numpy as np

from scipy.stats import geom
import matplotlib.pyplot as plt


#设置几何分布的参数
p = 0.5
dist =geom(p)

#设置采样范围
x = np.linspace(0, 5, 1000)

#获取几何分布的PMF和CDF
pmf = dist.pmf(x)
cdf = dist.cdf(x)

#随机采样500个值
sample = dist.rvs(500)



#绘图
plt.plot(x, pmf, x, cdf)

plt.grid()
plt.legend(['pmf','cdf'])
plt.show()






