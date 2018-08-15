#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = "tongzi"

'''
斐波那契数列
'''
import logging

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
		
	def __getitem__(self,n):
		if(isinstance(n,int)):
			a,b = 1,1
			for x in range(n):
				a,b = b,a+b
			return a
		if(isinstance(n,slice)):
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a, b = 1, 1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a, b = b, a + b
			return L
		
		
		
if __name__ == "__main__":
	for n in Fib():
		print(n)
	try:
		n = 0
		assert n!=0,'n is zero!'
		r = 10 / n
		print(r)
	except ZeroDivisionError as e:
		#print("Exception:",e)
		logging.exception(e)
	else:
		print("No Exception!")
	finally:
		print("Release resource..")
		
		
		