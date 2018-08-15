#!/usr/bin/env python3
#-*- coding:utf-8 -*-



__author__ = 'tongzi'

if __name__ == "__main__":
	with open(r'./io.py','r') as f:
		s = f.read()
		while s:
			print(s)
			s = f.read()
