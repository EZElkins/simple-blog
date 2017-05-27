#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

# ' url handlers '

import asyncio

from coroweb import get, post
from models import User

@get('/')
async def index(request):
    users = await User.findAll()
    # print(users)
    return {
        '__template__': 'index.html',
        'users': users
    }