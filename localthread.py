#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = "tongzi"

import threading

local_thread = threading.local()

class Student(object):
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def __str__(self):
		return "Student-->> name: %s, age: %s" % (self.name,self.age)
	__repr__ = __str__

def process_student():
	std = local_thread.student
	print("Hello, %s in (%s)" % (std,threading.current_thread().name))
	
def process_thread(name):
	local_thread.student = name
	process_student()
	
if __name__ == "__main__":
	t1 = threading.Thread(target=process_thread,args=(Student('Alice',21),),name="Thread-A")
	t2 = threading.Thread(target=process_thread,args=(Student('Bob',22),),name="Thread-B")
	
	t1.start()
	t2.start()
	
	t1.join()
	t2.join()
	ss = [1,2,3,4,5,6]
	f = lambda:ss
	print(f())
	
	
	

	