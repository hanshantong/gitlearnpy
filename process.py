#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = "tongzi"

from multiprocessing import Process
import os

def run_proc(name):
	print("Run child process %s (%s)..." % (name,os.getpid()))
	
	
if __name__ == "__main__":
	print("Parenr process %s." % (os.getpid()))
	p = Process(target=run_proc,args=('test',))
	print("Child process will start...")
	p.start()
	p.join()
	print("Child process end running...")