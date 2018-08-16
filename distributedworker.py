#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = "tongzi"

import time,sys,queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
	pass


QueueManager.register('get_task_queue')	
QueueManager.register('get_result_queue')

#连接到运行distributedtask.py的机器
server_address = '127.0.0.1'
print("Connect to %s server..." % server_address)

m = QueueManager(address = (server_address,58888),authkey=b'123')
m.connect()

task_q = m.get_task_queue()
result_q = m.get_result_queue()
for i in range(10):
	try:
		n = task_q.get(timeout=3)
		print("run task %d * %d" % (n,n))
		r = '%d * %d = %d' % (n,n,n*n)
		time.sleep(1)
		result_q.put(r)
	except queue.Empty:
		print('task queue is empty.')
		
print("worker exit.")

	
	
	
	