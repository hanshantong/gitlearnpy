#!/usr/bin/env python3
#-*- coding:utf-8 -*- 

import matplotlib.pyplot as plt

plt.figure(1)#第一幅图像
plt.subplot(2,1,1)
plt.plot([1,2,3])
plt.subplot(2,1,2)
plt.plot([4,5,6])

plt.figure(2)#第二幅图像
plt.subplot(2,1,1)
plt.plot([4,5,6])

plt.figure(1)#回到第一幅图像
plt.subplot(2,1,1)#回到子图(2,1,1)
plt.title('Easy as 1,2,3')#子图(2,1,1)的标题

plt.show()

'''
可以使用函数clf()清除当前的figure，使用cla()函数清除当前的axes

'''