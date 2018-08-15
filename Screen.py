#!/usr/bin/env python3
#-*- coding:utf-8 -*-

class Screen(object):
	@property
	def width(self):
		return self._width
		
	@width.setter
	def width(self,w):
		self._width = w
		
	@property
	def height(self):
		return self._height
		
	@height.setter
	def height(self,w):
		self._height = w
	
	@property
	def resolution(self):
		return str(self._width) + " x " + str(self._height)
		
	def print_info(self):	
		print("width:%s, height: %s, resolution: %s"%(self._width,self._height,self.resolution))
		
if __name__ == "__main__":
	s = Screen()
	s.width = 100
	s.height = 200
	s.print_info()
	
	
	