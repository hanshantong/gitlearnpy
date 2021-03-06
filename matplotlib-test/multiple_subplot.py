#!/usr/bin/env python3
#-*- coding:utf-8 -*- 

import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

mpl.rc('lines', linewidth=1, color='b')

#设置样式
#plt.style.use(['dark_background', 'presention']) #组合样式
plt.style.use('ggplot')

x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)

y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)

'''
with plt.style.context(('dark_background')):#限制style的范围：仅作用早subplot(2, 1, 1)
	plt.subplot(2, 1, 1)
	
'''	
plt.subplot(2, 1, 1)
plt.plot(x1, y1, 'o-')

#Latex语法：必须以r打头，用两个$符号将LaTeX表达式包含起来
#如下所示:r"$cos(2{\pi}t)e^{-t}$"
plt.title(r"$cos(2{\pi}t)e^{-t}$")
plt.ylabel('Damped oscillation')

plt.subplot(2, 1, 2)
plt.plot(x2, y2, '.-')
plt.xlabel('time (s)')
plt.ylabel('Undamped')
plt.title(r"$cos(2{\pi}t)$")
plt.savefig('multiple_subplot.png')

plt.show()








