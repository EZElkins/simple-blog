#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
import datetime as dt

from aiohttp import web

host = '127.0.0.1'
port = 9000

def index(request):
	return web.Response(body='<h1>Home Page...</h1>', content_type='text/html')

async def init(loop):
	app = web.Application(loop=loop)
	app.router.add_route('GET', '/', index)
	srv = await loop.create_server(app.make_handler(), host, port)
	logging.info('server started at http://%s:%s...' % (host, port))
	return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()