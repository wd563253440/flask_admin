# -*- coding: utf-8 -*-
"""
-----------------------------------------------
@version 3.7
@time 2021/3/25 16:31
@author passion.wangd
@title
@file user.py
@IDE PyCharm
-----------------------------------------------
"""
from flask_restful import Resource
from flask import Response
import json
from app.models.management.user import UserModel


class User(Resource):

    def __init__(self, state, name, head_img_url, mobile, salt, password, created, edited, deleted):
        pass

    def __repr__(self):
        return '<User %r>' % self.username

    def get(self, id):
        """
        @@@
        ### args
        | args | nullable | type | remark |
        |--------|--------|--------|--------|
        |    id    |    false    |    int   |    todo id    |
        ### return
        - #### json
        > {......}
        @@@
        """
        data = UserModel.query.all()
        print(data)
        resp = Response(response=data, status=200, mimetype="application/json")
        return resp

    def post(self):
        data = UserModel.query.all()
        print(data)
        resp = Response(response=data, status=200, mimetype="application/json")
        return resp


class Users(Resource):
    def get(self):
        data = json.dumps({
            'name': 'wd',
        })
        resp = Response(response=data, status=200, mimetype="application/json")
        return resp

    def post(self):
        pass
