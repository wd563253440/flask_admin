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


class User(Resource):

    def get(self, id):
        data = json.dumps({
            'name': 'wd',
            'id': id
        })
        resp = Response(response=data, status=200, mimetype="application/json")
        return resp

    def post(self):
        pass


class Users(Resource):
    def get(self):
        data = json.dumps({
            'name': 'wd',
        })
        resp = Response(response=data, status=200, mimetype="application/json")
        return resp

    def post(self):
        pass
