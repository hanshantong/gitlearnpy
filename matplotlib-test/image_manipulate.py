#!/usr/bin/env python3
#-*- coding:utf-8 -*- 

import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import matplotlib.image as mpimg


img = mpimg.imread('stinkbug.png')#读入图片

#imgplot = plt.imshow(img)

lum_img = img[:,:,0]

#plt.imshow(lum_img, cmap='hot')
#plt.imshow(lum_img)
#plt.set_cmap('nipy_spectral')
#plt.colorbar() #当改变colormap时，必须重新创建颜色条

#创建图片条形图，展示颜色的分布情况
#plt.hist(lum_img.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')

#imgplot = plt.imshow(lum_img, clim=(0.0, 0.7))

fig = plt.figure()
a = fig.add_subplot(1, 2, 1)
imgplot = plt.imshow(lum_img)
a.set_title('Before')
plt.colorbar(ticks=[0.1, 0.3, 0.5, 0.7], orientation='horizontal')

a = fig.add_subplot(1, 2, 2)
imgplot = plt.imshow(lum_img)
imgplot.set_clim(0.0, 0.7)
a.set_title('After')
plt.colorbar(ticks=[0.1, 0.3, 0.5, 0.7], orientation='horizontal')


plt.show()


