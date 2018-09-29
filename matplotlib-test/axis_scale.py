#!/usr/bin/env python3
#-*- coding:utf-8 -*- 

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import NullFormatter

np.random.seed(19680801)

#正态分布，均值为loc，方差为scale，个数为size
y = np.random.normal(loc=0.5, scale=0.5,size=1000)

#提取y中大于0小于1的
y = y[(y >0) & (y <1)]
y.sort()
x = np.arange(len(y))

#start plotting figure
plt.figure(1)

#现行坐标系
plt.subplot(2,2,1)
plt.plot(x, y)
plt.yscale('linear')
plt.title('linear')
plt.grid(True)#绘制网格

#对数坐标 log
plt.subplot(2,2,2)
plt.plot(x, y)
plt.yscale('log')
plt.title('log')
plt.grid(True)

#symmetric log
plt.subplot(2,2,3)
plt.plot(x, y-y.mean())
plt.yscale('symlog', linthreshy=0.01)
plt.title('symlog')
plt.grid(True)


#logit
plt.subplot(2,2,4)
plt.plot(x, y)
plt.yscale('logit')
plt.title('logit')
plt.grid(True)

plt.gca().yaxis.set_minor_formatter(NullFormatter())

plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, 
hspace=0.25, wspace=0.35)

plt.show()












