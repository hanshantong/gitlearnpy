#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = "tongzi"

import socket
import threading
import time

def tcplink(sock,addr):	
	print("Accepted a new connection from (%s,%s)" % addr)
	sock.send(b"Welcome")
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if not data or data.decode('utf-8') == 'exit':
			break;
		sock.send(("Hello, %s" % data.decode('utf-8')).encode('utf-8'))
	sock.close()
	print("Connection from (%s,%s) closed." % addr)


#创建一个socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#绑定到指定的地址：（IP,PORT）
s.bind(('127.0.0.1',58888))

#监听端口
s.listen(5)  #参数表示等待连接的最大数量
print("Waiting client connect ...")

#客户端连接后，开启线程去处理他们之间的交互
while True:
	sock,addr = s.accept()
	
	t = threading.Thread(target=tcplink,args=(sock,addr))
	t.start()
	
	

	
	
	
	
	
	
	
	
	
	
	
	