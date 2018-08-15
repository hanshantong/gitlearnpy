#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = "tongzi"

'''
斐波那契数列
'''

class Fib:
	def __init__(self):
		self.a,self.b = 0,1 #初始化两个计数器a，b
	
	def __iter__(self):
		return self
	
	
	def __next__(self):
		self.a,self.b = self.b,self.a + self.b
		
		if self.a > 10000:  #退出循环的条件
			raise StopIteration()
		return self.a
	
if __name__ == "__main__":
	for n in Fib():
		print(n)
		
		
		