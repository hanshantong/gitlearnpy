#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = "tongzi"

import random,time,queue
from multiprocessing.managers import BaseManager

#发送任务的队列
task_queue = queue.Queue()

#获取结果的队列
result_queue = queue.Queue()

def return_task_queue():
	global task_queue
	return task_queue
	
def return_result_queue():
	global result_queue
	return result_queue

class QueueManager(BaseManager):
	pass
	
#pickle模块不能序列化lambda function,该写法在ubuntu16.04 LTS下可以正常工作
#QueueManager.register('get_task_queue',callable=lambda:task_queue)
#QueueManager.register('get_result_queue',callable=lambda:result_queue)

QueueManager.register('get_task_queue',callable=return_task_queue)
QueueManager.register('get_result_queue',callable=return_result_queue)

manager = QueueManager(('',58888),authkey=b'123') #绑定到端口8888

manager.start()

task_q = manager.get_task_queue()
result_q = manager.get_result_queue()

for i in range(8):	
	n = random.randint(0,100)
	print("Put task_q %d.." % n)
	task_q.put(n)
	
print("Get results:")
for i in range(10):
	r = result_q.get(timeout=10)
	print("Got result is %s" % r)
	
manager.shutdown()
print("manager exited")

