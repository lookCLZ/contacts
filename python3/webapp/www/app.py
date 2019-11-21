#!/usr/local/bin/python3
__author__ = 'Hongrui'
import sys
sys.path.append('/usr/local/lib/python3.7/site-packages')

import logging;logging.basicConfig(level=logging.INFO)

import asyncio,os,json,time
from aiohttp import web


from datetime import datetime


print(__name__)
def index(request):
    return web.Response(body=b'<h1>awefont</h1>',content_type="text/html")

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('服务已启动：http://127.0.0.1:9000')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()