#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = 'tongzi'

import numpy as np

import matplotlib.pyplot as mpl

from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial.distance import pdist, squareform

import scipy.cluster.hierarchy as hy

def clusters(number=20, cnumber=5, csize = 10):
	rnum = np.random.randn(cnumber ,2)
	
	#处理第0列
	rn = rnum[:,0] * number
	rn = rn.astype(int)  #转为整数
	rn[np.where(rn < 5)] = 5  #将rn中小于5的元素逗赋值为5
	rn[np.where(rn > number/2.0)] = round(number / 2., 0)
	
	#处理第1列
	ra = rnum[:,1]
	ra[np.where(ra < 1.5)] = 1.5
	
	cls = np.random.randn(number, 3) * csize
	
	rxyz = np.random.randn(cnumber-1, 3)
	for i in range(cnumber-1):
		tmp = np.random.randn(rn[i+1], 3)
		x = tmp[:,0] + (rxyz[i,0] * csize)
		y = tmp[:,0] + (rxyz[i,1] * csize)
		z = tmp[:,0] + (rxyz[i,2] * csize)
		tmp = np.column_stack([x,y,z])
		cls = np.vstack([cls,tmp])
	return cls
	

cls = clusters()
D = pdist(cls[:,0:2])	
D = squareform(D)

#绘图
fig = mpl.figure(figsize=(8,8))
ax1 = fig.add_axes([0.09, 0.1, 0.2, 0.6])
Y1 = hy.linkage(D, method='complete')
cutoff = 0.3 * np.max(Y1[:,2])
Z1 = hy.dendrogram(Y1, orientation='right', color_threshold=cutoff)
ax1.xaxis.set_visible(False)
ax1.yaxis.set_visible(False)

ax2 = fig.add_axes([0.3, 0.71, 0.6, 0.2])
Y2 = hy.linkage(D, method='average')
cutoff = 0.3 * np.max(Y2[:,2])
Z2 = hy.dendrogram(Y2, color_threshold=cutoff)
ax2.xaxis.set_visible(False)
ax2.yaxis.set_visible(False)

#绘制距离矩阵
ax3 = fig.add_axes([0.3,0.1,0.6,0.6])
idx1 = Z1['leaves']
idx2 = Z2['leaves']

D = D[idx1,:]
D = D[:,idx2]
ax3.matshow(D, aspect='auto',origin='lower',cmap=mpl.cm.YlGnBu)
ax3.xaxis.set_visible(False)
ax3.yaxis.set_visible(False)


fig.savefig('cluster_hy_f01.pdf',bbox='tight')






