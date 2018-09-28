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

def group(data, index):
	number = np.unique(index) #去除index中的重复数据，并排序
	groups = []
	for i in number:
		groups.append(data[index == i])
	return groups


cls = clusters()

#计算连接矩阵
Y= hy.linkage(cls[:,0:2], method='complete')	

cutoff = 0.3 * np.max(Y[:,2])
index = hy.fcluster(Y, cutoff, 'distance')

groups = group(cls, index)

fig = mpl.figure(figsize=(6, 6))
ax = fig.add_subplot(111)
colors = ['r','c','b','g','orange','k','y','gray']

for i, g in enumerate(groups):
	i = np.mod(i, len(colors))
	ax.scatter(g[:,0], g[:,1],c=colors[i], edgecolor='none', s=50)
	ax.xaxis.set_visible(False)
	ax.yaxis.set_visible(False)
	
fig.savefig('cluster_hy_f02.pdf',bbox='tight')	