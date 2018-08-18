#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = "tongzi"

import socket 


'''
AF_INET表示IPv4,AF_INET6表示IPv6，SOCK_STREAM表示使用面向流的TCP协议
'''
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#连接到对应的IP地址
s.connect(('www.sina.con.cn',80))

#发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

#接收数据
buffer = []
while True:
	d = s.recv(1024) #每次接收1K字节
	if d:
		buffer.append(d)
	else:
		break;
	
data = b''.join(buffer)

#关闭连接
s.close()

#处理数据
header, html = data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))

with open('sina.html','wb') as f:
	f.write(html)
