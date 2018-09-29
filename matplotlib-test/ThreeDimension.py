#!/usr/bin/env python3
#-*- coding:utf-8 -*- 

import matplotlib.pyplot as plt
import numpy as np

#注册3D投影
from mpl_toolkits.mplot3d import Axes3D


from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

fig = plt.figure()
ax = fig.gca(projection='3d')

X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

#绘制表面
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
						linewidth=0, antialiased=False)

ax.set_zlim(-1.01, 1.01)#Z轴范围
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

#颜色条
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()


