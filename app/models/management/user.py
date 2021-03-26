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

class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(1))
    name = db.Column(db.String(255))
    head_img_url = db.Column(db.String(255))
    mobile = db.Column(db.String(11))
    salt = db.Column(db.String(64))
    password = db.Column(db.Date)
    created = db.Column(db.String(64))
    edited = db.Column(db.Date)
    editor = db.Column(db.String(64))
    deleted = db.Column(db.String(1))
