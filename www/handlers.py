#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

# ' url handlers '

import asyncio, time

from coroweb import get, post
from models import User, Blog

@get('/users')
async def users(request):
    users = await User.findAll()
    # print(users)
    return {
        '__template__': 'index.html',
        'users': users
    }


@get('/')
def index(request):
    summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    blogs = [
        Blog(id='1', name='Test Blog', summary=summary, created_at=time.time()-120),
        Blog(id='2', name='Something New', summary=summary, created_at=time.time()-3600),
        Blog(id='3', name='Learn Swift', summary=summary, created_at=time.time()-7200)
    ]
    return {
        '__template__': 'blogs.html',
        'blogs': blogs
    }