#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = 'tongzi'

import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt


line = lambda x: x + 3

solution = fsolve(line, -2)
print(solution)

#寻找两个函数的交点
def findIntersection(func1, func2, x0):
	return fsolve(lambda x:func1(x) - func2(x),x0)
	

funky = lambda x: np.cos(0.2*x) * np.sin(x / 2)

line = lambda x: 0.01*x - 0.5

ans = findIntersection(funky, line, [15,20,30,35,40,45,65])
print(ans,line(ans))


#绘制曲线
x = np.linspace(0,60,10000)	

plt.plot(x,funky(x),x,line(x))

#标注
plt.legend(['funky','line'])

#网格
plt.grid()

#显示曲线
plt.show()