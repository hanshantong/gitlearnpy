#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = "tongzi"

from multiprocessing import Process,Queue
import os,time,random

def write(q):
	print("Process to write: %s" % os.getpid())
	for val in ['A','B','C']:
		print("Put %s to queue." % val)
		q.put(val)
		time.sleep(random.random() * 5)
		

		
def read(q):
	print("Process to read %s:" % os.getpid())
	while True:
		val = q.get(True)
		print("Get %s from queue." % val)
		time.sleep(random.random() * 5)
		
if __name__ == "__main__":
	q = Queue()
	pw = Process(target=write,args=(q,))
	pr = Process(target=read,args=(q,))
	
	pw.start()
	pr.start()
	
	pw.join()
	pr.join()
	
	pr.terminate() #因为read函数有个死循环
	
	
	
	
	