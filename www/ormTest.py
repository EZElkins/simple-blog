#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

import asyncio, orm
from models import User, Blog, Comment


loop = asyncio.get_event_loop()

# 测试
async def test():
    await orm.create_pool(loop, user='robot', password='123456', db='simple_blog')
    # u = User(name='Niconico', email='niconico@litesama.com', passwd='66612345', avatar='https://pic2.zhimg.com/03de795a287804b133c6eefdc9325a31_xl.jpg')
    u = User(name='Elkins', email='elkins@litesama.com', passwd='135246', avatar='https://pic2.zhimg.com/03de795a287804b133c6eefdc9325a31_xl.jpg')
    await u.save()
    r = await User.findAll()
    print(r)

loop.run_until_complete(test())
loop.close()
