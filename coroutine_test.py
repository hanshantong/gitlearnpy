#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = "tongzi"

def consumer():
	r = ''
	while True:
		n = yield r
		if not n:
			return
		print('[Consumer] Consuming %s...' % n)
		r = '200 OK'
		
def produce(c):
	c.send(None)  #启动生成器
	n = 0
	while n < 10:
		n = n + 1
		print('[Producer] Producing %s...' % n)
		r = c.send(n)
		print('[Producer] Consumer return %s' % r)
		
	c.close()


if __name__ == "__main__":
	c = consumer()
	produce(c)