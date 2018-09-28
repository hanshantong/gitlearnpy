#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = 'tongzi'

import numpy as np
from scipy.sparse.linalg import eigsh
from scipy.linalg import eigh

import scipy.sparse
import time


N = 3000

#创建一个稀疏矩阵
m = scipy.sparse.rand(N, N)

#复制矩阵m
a = m.toarray()

print('The numpy array data size: ' + str(a.nbytes) + 'byte(s)')
print('The sparse matrix data size: ' + str(m.data.nbytes) + 'byte(s)')

#非稀疏矩阵
to = time.time()
res1 = eigh(a)
dt = str(np.round(time.time() - to, 3)) + 'second(s)'
print('Non-sparse operation takes ' + dt)

#稀疏矩阵
to = time.time()
res2 = eigsh(m)
dt = str(np.round(time.time() - to, 3)) + 'second(s)'
print('Sparse operation takes ' + dt)
