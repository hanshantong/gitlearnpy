#!/usr/bin/env python3
#-*- coding:utf-8 -*- 

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter
plt.ioff()
plt.rcParams.update({'figure.autolayout':True})

data = {'Barton LLC': 109438.50,
        'Frami, Hills and Schmidt': 103569.59,
        'Fritsch, Russel and Anderson': 112214.71,
        'Jerde-Hilpert': 112591.43,
        'Keeling LLC': 100934.30,
        'Koepp Ltd': 103660.54,
        'Kulas Inc': 137351.96,
        'Trantow-Barrows': 123381.38,
        'White-Trantow': 135841.99,
        'Will LLC': 104437.60}
		
group_data = list(data.values())
group_names = list(data.keys())
group_mean = np.mean(group_data)


def currency(x, pos):
	'''The two args are the value and tick position'''
	if x >= 1e6:
		s = '${:1.1f}M'.format(x * 1e-6)
	else:
		s = '${:1.0f}K'.format(x * 1e-3)
	return s

formatter = FuncFormatter(currency)	


#plt.style.use('presention')
plt.style.use('fivethirtyeight')
#plt.style.use('ggplot')


fig, ax = plt.subplots(figsize=(12, 8))
ax.barh(group_names,group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')

#添加一条竖线，位置是数据的平均值
ax.axvline(group_mean, ls='--', color='r')

#标记那些新公司:在group_names中3,5,8对应是新公司
for group in [3, 5, 8]:
	ax.text(145000, group, 'New Company', fontsize=10, verticalalignment='center')

ax.title.set(y=1.05)#标题上移
	
ax.set(xlim=[-10000,140000], xlabel='Total Revenue', ylabel='Company',
		title='Company Revenue')

ax.xaxis.set_major_formatter(formatter)
#设置x轴的刻度标记
ax.set_xticks([0, 25e3, 50e3, 75e3, 100e3, 125e3])
#fig.subplots_adjust(right=.1)

#transparent=True makes the background of the saved figure transparent if the format supports it.
#dpi=80 controls the resolution (dots per square inch) of the output.
#bbox_inches="tight" fits the bounds of the figure to our plot.
fig.savefig('sale.png', transparent=True, dpi=300, bbox_inches='tight')

plt.draw()
plt.show()





