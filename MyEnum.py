#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = 'tongzi'

from enum import Enum,unique

Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))



@unique  #该装饰器保证枚举值没有重复值
class Weekday(Enum):
	Sun = 0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6




if __name__ == "__main__":
	print(Month.Jan)
	for n,m in Month.__members__.items():
		print(n,'=>',m,',',m.value)

	print(Weekday.Mon)	
		
		