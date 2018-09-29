#!/usr/bin/env python3
#-*- coding:utf-8 -*- 

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def my_plotter(ax, data1, data2, param_dict):
	'''
	A helper function to make a graph

	Parameters
	---------
	ax: Axes
	    The axes to draw to
	
	data1: array
	    The x data
	
	data2: array	
	    The y data
	
	param_dict: dict
	     Dictionary of kwargs to pass to ax.plot
		 
	Returns
	--------
	out: list
	     list of artist added

	'''
	out = ax.plot(data1, data2, **param_dict)
	
	
	
data1, data2, data3, data4 = np.random.randn(4, 100)	
fig, (ax1, ax2) = plt.subplots(1, 2)
my_plotter(ax1, data1, data2, {'marker':'x'})
my_plotter(ax2, data3, data4,{'marker':'o'})
plt.show()

ax = plt.gca()#获取当前的axes，gca->get current axes
fig= plt.gcf() #获取当前的图表， gcf->get current figure
