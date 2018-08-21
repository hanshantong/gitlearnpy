#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = "tongzi"

import asyncio

async def http_get(domain):
	reader, writer = await asyncio.open_connection(domain, 80)
	
	writer.write(b'\r\n'.join([
		b'GET / HTTP/1.1',
		b'Host: %b' % domain.encode('utf-8'),
		b'Connection: close',
		b'',b''
	]))
	
	async for line in reader:
		print('>>>', line)
	
loop = asyncio.get_event_loop()
try:
	loop.run_until_complete(http_get('www.sina.com.cn'))
finally:
	loop.close()