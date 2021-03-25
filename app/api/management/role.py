# -*- coding: utf-8 -*-
"""
-----------------------------------------------
@version 3.7
@time 2021/3/25 18:45
@author passion.wangd
@title
@file role.py
@IDE PyCharm
-----------------------------------------------
"""
from flask_restful import Resource
from flask import Response
import json


class Role(Resource):

    def get(self, id):
        data = json.dumps({
            'role': 'wd',
            'id': id
        })
        resp = Response(response=data, status=200, mimetype="application/json")
        return resp

    def post(self):
        pass


class Roles(Resource):
    def get(self):
        data = json.dumps({
            'role': 'wd',
        })
        resp = Response(response=data, status=200, mimetype="application/json")
        return resp

    def post(self):
        pass
