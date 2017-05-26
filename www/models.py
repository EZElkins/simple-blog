#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

from orm import Model, StringField, IntegerField, TextField, BooleanField


class User(Model):
    __table__ = 'users'

    id = IntegerField(primary_key=True)
    name = StringField()