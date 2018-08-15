#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = "tongzi"

import time,threading
def loop():
	print("Thread %s is running..." % threading.current_thread().name)
	n = 0
	while n < 10:
		n = n + 1
		print("Thread %s -->>> %s" % (threading.current_thread().name,n))
		time.sleep(1)
	print("Thread %s stoped" % threading.current_thread().name)
	
print("Thread % s is running.. " % threading.current_thread().name)
t = threading.Thread(target=loop,name="LoopThread")
t.start()
t.join()
print("Thread % s stoped.. " % threading.current_thread().name)

	