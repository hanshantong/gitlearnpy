#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = "tongzi"

import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

for data in [b'Michael',b'Mishiel',b'Alice']:
	#发送数据
	s.sendto(data,('127.0.0.1',8888))
	print(s.recv(1024).decode('utf-8'))
s.close()