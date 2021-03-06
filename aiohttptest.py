#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = "tongzi"

import asyncio
from aiohttp import web

async def index(request):
	await asyncio.sleep(0.5)
	return web.Response(body=b'<h1>Index</h1>')
	
async def hello(request):
	await asyncio.sleep(0.5)
	text = '<h1>hell0, %s</h1>' % request.match_info['name']
	return web.Response(body = text.encode('utf-8'))
	
async def init(loop):
	app = web.Application(loop=loop)
	app.router.add_route('GET', '/', index)
	app.router.add_route('GET', '/hello/{name}', hello)
	srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8888)
	print('Server started at http://127.0.0.1:8888...')
	return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()