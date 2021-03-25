# -*- coding: utf-8 -*-
"""
-----------------------------------------------
@version 3.7
@time 2021/3/25 17:53
@author passion.wangd
@title
@file user.py
@IDE PyCharm
-----------------------------------------------
"""
from app.models.db import db

class UserModel(db.model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password
