#!/usr/bin/env python3
#-*- coding:utf-8 -*- 

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import RadioButtons

t = np.arange(0.0, 2.0, 0.01)
s0 = np.sin(2*np.pi*t)
s1 = np.sin(4*np.pi*t)
s2 = np.sin(8*np.pi*t)

fig, ax = plt.subplots()
line,=ax.plot(t, s0, lw=2, color='red')
plt.subplots_adjust(left=0.3)

axcolor = 'lightgoldenrodyellow'
rax = plt.axes([0.05, 0.7, 0.15, 0.15], facecolor=axcolor)
radio = RadioButtons(rax, ('2 Hz', '4 Hz', '8 Hz'))

def hzFunc(label):
	hzdict = {'2 Hz':s0, '4 Hz':s1, '8 Hz':s2}
	ydata = hzdict[label]
	line.set_ydata(ydata)
	plt.draw()
radio.on_clicked(hzFunc)

rax = plt.axes([0.05, 0.4, 0.15, 0.15], facecolor=axcolor)
radio2 = RadioButtons(rax, ('red', 'blue', 'green'))

def colorFunc(label):
	line.set_color(label)
	plt.draw()
radio2.on_clicked(colorFunc)

rax = plt.axes([0.05, 0.1, 0.15, 0.15], facecolor=axcolor)
radio3 = RadioButtons(rax, ('-', '--', '-.', 'steps', ':'))

def styleFunc(label):
	line.set_linestyle(label)
	plt.draw()
radio3.on_clicked(styleFunc)

plt.show()

