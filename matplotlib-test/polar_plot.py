#!/usr/bin/env python3
#-*- coding:utf-8-*-

import numpy as np 
import matplotlib.pyplot as plt

T = np.linspace(0, 2 * np.pi, 4096)
plt.axes(polar=True)
plt.plot(T, 1. + 0.25 * np.sin(16 * T), c = 'r')
plt.savefig('sin_polar.pdf')
plt.show()
