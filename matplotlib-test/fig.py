#!/usr/bin/env python3
#-*- coding:utf-8 -*- 

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#an empty figure with no axes
fig = plt.figure()

#Add a title so we know which it is
fig.suptitle('No axes on this figure')

#a figure with a 2 X 2 grid of Axes
fig, ax_lst = plit.subplots(2, 2)

#convert DataFrame to array
df = pd.DataFrame(np.random.randn(4,5), columns=list('abcde'))
df_asndarray = df.values

#convert np.matrix to np.array
b = np.matrix([[1,2], [3,4]])
b_asndarray = np.asarray(b)
