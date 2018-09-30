#!/usr/bin/env python3
#-*- coding:utf-8 -*- 

import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import matplotlib.image as mpimg

fig = plt.figure()
rect = fig.patch

rect.set_facecolor('lightgoldenrodyellow')
ax1 = fig.add_axes([0.1, 0.3, 0.4, 0.4])
rect = ax1.patch
rect.set_facecolor('lightslategray')

for label in ax1.xaxis.get_ticklabels():
	label.set_color('red')
	label.set_rotation(45)
	label.set_fontsize(16)
	
for line in ax1.yaxis.get_ticklines():
	line.set_color('blue')
	line.set_markersize(3)
	line.set_markeredgewidth(1)
	
plt.show()
