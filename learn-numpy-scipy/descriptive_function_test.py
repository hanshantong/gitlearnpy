#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = 'tongzi'

import numpy as np

from scipy import stats

#产生100个正太分布采样点
sample = np.random.randn(100)

#the harmonic mean:调和平均数
#每一项的数据必须大于0
out = stats.hmean(sample[sample > 0])
print('Harmonic mean = ' + str(out))


#截尾均值
#计算大于1小于-1区间的均值
out = stats.tmean(sample, limits=(-1, 1))
print('\nTrimmed mean = ' + str(out))


#计算样本的偏度
out = stats.skew(sample)
print('\nSkewness = ' + str(out))


#综合性的函数，可以给出样本全方面的信息
out = stats.describe(sample)
print('\nSize = ' + str(out[0]))
print('Min = ' + str(out[1][0]))
print('Max = ' + str(out[1][1]))
print('Mean = ' + str(out[2]))
print('Variance = ' + str(out[3]))
print('Skewness = ' + str(out[4]))  #偏度
print("Kurtosis = " + str(out[5]))  #峰度







