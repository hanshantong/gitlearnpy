#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = 'tongzi'

import numpy as np

from scipy import stats

#产生100个标准正太分布的采样点
sample = np.random.randn(100)


#使用normaltest测试零假设
out = stats.normaltest(sample)
print('normaltest output')

print('Z-score = ' + str(out[0]))
print('P-value = ' + str(out[1]))


#使用kstest（柯尔莫诺夫-斯米尔诺夫校验）
#这里讲KS和正太分布比较
#这里的D是KS的统计值，它越接近0越好
out = stats.kstest(sample, 'norm')
print('kstest output for the Normal distribution')
print('D = ' + str(out[0]))
print('P-value = ' + str(out[1]))


#类似的，kstest还可以和其它分布比较
out = stats.kstest(sample, 'wald')
print('kstest output for the Wald distribution')
print('D = ' + str(out[0]))
print('P-value = ' + str(out[1]))





