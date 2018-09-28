#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = 'tongzi'

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


#采样范围
x = np.linspace(-5, 5, 1000)

#创建一个标准正太分布
#其中参数loc是均值， scale是标准差
dist = norm(loc=0, scale=1)

#retrieving norm's pdf and cdf
#获取标准正太分布的概率密度函数和累计分布函数
pdf = dist.pdf(x) #结果是numpy.ndarray类型的数据
cdf = dist.cdf(x) #结果是numpy.ndarray类型的数据

#随机变量采样（random variable sample）
sample = dist.rvs(500)

#绘图
plt.plot(x, pdf , x, cdf)

plt.legend(['pdf','cdf'])
plt.grid()
plt.show()