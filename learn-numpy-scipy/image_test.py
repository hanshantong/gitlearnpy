#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = 'tongzi'

import numpy as np
from scipy.misc import imread, imsave
from glob import glob

#获取一系列图片
files = glob('space/*.JPG')

#读取第一个图像文件，并将其转为np.float32
im1 = imread(files[0]).astype(np.float32)

for i in range(len(1,files)):
	im1 += imread(files[i]).astype(np.float32)
	
#保存
imsave('stacked_image.jpg',im1)	
