#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = "tongzi"

#从wsgire导入
from wsgiref.simple_server import make_server

#导入我们编写的application()函数
from hello_application import application

#创建一个HTTP服务器，IP地址为空，端口是8888，处理函数是application
httpd = make_server('', 8888, application)
print('Serving HTTP on port 8888...')

#开始监听HTTP请求
httpd.serve_forever()