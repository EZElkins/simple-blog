#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

import asyncio, orm
from models import User


loop = asyncio.get_event_loop()

# 插入
async def insert():
    await orm.create_pool(loop, user='root', password='yishiyanhuo', db='Simple_Blog')
    u = User(id=2, name='Avril')
    await u.save()
    r = await User.findAll()
    print(r)


loop.run_until_complete(insert())
loop.close()
