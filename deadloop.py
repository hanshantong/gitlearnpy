#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = "tongzi"
import threading,multiprocessing


def loop():
	x = 0
	while True:
		x = x ^ 1
	
	
print("The number of cpu core is: ",multiprocessing.cpu_count())

for i in range(multiprocessing.cpu_count()):
	t = threading.Thread(target=loop)
	t.start()