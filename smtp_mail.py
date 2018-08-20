#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = "tongzi"

from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
import getpass

import smtplib

def format_addr_me(s):
	name, addr = parseaddr(s)
	return formataddr((Header(name,'utf-8').encode(), addr))

#输入要发送邮件的email地址和密码
from_addr = input('From:')
passwd = getpass.getpass('Password:')

#输入收件人地址，可以输入多个
to_addr = input("To:")

#输入SMTP服务器的地址
smtp_server = input('SMTP server:')	
	
	
	
msg = MIMEText('Hello, send by Python. Author: tongzi [2018/08/20]', 'plain', 'utf-8')
msg['From'] = format_addr_me("Tongzi <%s>" % from_addr)
msg['To'] = format_addr_me('山楂 <%s>' % to_addr)
msg['Subject'] = Header("来自Tongzi的问候。。。",'utf-8').encode()





server = smtplib.SMTP(smtp_server, 25)  #SMTP协议的默认端口是25
server.set_debuglevel(1)
server.login(from_addr,passwd)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()


