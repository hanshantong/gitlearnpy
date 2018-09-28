#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = 'tongzi'

import numpy as np

x = np.random.randn(100)

#统计
#均值
mean = x.mean()

#标准差
std = x.std()

#方差
var = x.var()

print("mean is {}, standard deviation is {}\n and variance is {}"
      .format(mean,std,var))


