#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = "tongzi"

import socket
import threading

def udp_process(addr,data):
	pass



s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#绑定到端口
s.bind(('127.0.0.1',8888))

print('Bind UDP on 8888')
while True:
	data, addr = s.recvfrom(1024)
	print('Received data from %s:%s' % addr)
	s.sendto(b'Hello, %s!' % data,addr)


