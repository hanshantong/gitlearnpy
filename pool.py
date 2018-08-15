#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = "tongzi"

from multiprocessing import Pool
import os,time,random
import sys

f = open("execute.txt",'a+')
sys.stdout = f

def long_time_task(name):
	print("Run task %s (%s)" % (name,os.getpid())) 
	start = time.time()
	print(randon.random() * 10)
	time.sleep(randon.random() * 10)
	end = time.time()
	print("Task %s runs %0.2f seconds." % (name,(end-start)))
	
if __name__ == "__main__":
	print("Parent process %s." % (os.getpid()))
	p = Pool(5)
	for i in range(5):
		p.apply_async(long_time_task,args=(i,))
	print("Waiting for all subprocesses done...")
	p.close()
	p.join()
	print("All subprocess done.")
	f.close()
	
	