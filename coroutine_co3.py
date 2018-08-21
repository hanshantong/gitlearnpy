#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = "tongzi"

import asyncio
import threading

@asyncio.coroutine
def wget(host):
	print('wget %s...' % host)
	connect = asyncio.open_connection(host, 80)
	reader, writer = yield from connect
	header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
	writer.write(header.encode('utf-8'))
	yield from writer.drain()
	while True:
		line = yield from reader.readline()
		if line == b'\r\n':
			break;
		print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
	
	#忽略body，直接关闭socket
	writer.close()
	
	
#获取EventLoop
loop = asyncio.get_event_loop()

#执行routine
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
	