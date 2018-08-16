#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = "tongzi"

import time,threading,random


balance = 0
lock = threading.Lock()  #create a lock

def change_it(n):
	global balance
	balance = balance + n
	balance = balance - n
	
def run_thread(n):
	for i in range(10):
		lock.acquire() #get a lock
		change_it(n)
		lock.release()  #release the lock
		time.sleep(random.random())

t1 = threading.Thread(target=run_thread,args=(3,))
t2 = threading.Thread(target=run_thread,args=(5,))

t1.start()
t2.start()

t1.join()
t2.join()

print(balance)