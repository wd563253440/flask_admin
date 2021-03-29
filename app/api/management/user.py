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
from datetime import datetime

from flask_restful import Resource, marshal_with, fields, abort
from flask import Response, request
import json

from app.models.db import db
from app.models.management.user import UserModel


class User(UserModel):
    def __init__(self, state=None, name=None, head_img_url=None, mobile=None, salt=None, password=None, created=None, creator=None, edited=None, editor=None, deleted=None):
        self.state = state
        self.name = name
        self.head_img_url = head_img_url
        self.mobile = mobile
        self.salt = salt
        self.password = password
        self.created = created
        self.creator = creator
        self.edited = edited
        self.editor = editor
        self.deleted = deleted


my_fields = {
    'state': fields.Integer,
    'name': fields.String,
    'head_img_url': fields.String,
    'mobile': fields.String,
    'salt': fields.String,
    'password': fields.String,
    'created': fields.DateTime,
    'creator': fields.String,
    'edited': fields.DateTime,
    'editor': fields.String,
    'deleted': fields.Integer
}


class UserView(Resource):

    @marshal_with(my_fields)
    def get(self, id):
        """
        @@@
        ### args
        | args | nullable | type | remark |
        |------|----------|------|--------|
        | id   |  false   | int  |todo id |
        ### return
        - #### json
        > {......}
        @@@
        """
        try:
            data = UserModel.query.filter_by(id=id).first()
            if data is None:
                return abort(404)
            return User(name=data.name, created=data.created)
        except Exception as e:
            abort(500)

    @marshal_with(my_fields)
    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        """
        @@@
        ### args
        | args | nullable | type | remark |
        |------|----------|------|--------|
        | id   |  false   | int  |todo id |
        ### return
        - #### json
        > {......}
        @@@
        """
        if not request.values:
            abort(404)
        params = request.values.to_dict()
        user = User(state=int(params['state']),
                    name=params['name'],
                    head_img_url=params['head_img_url'],
                    mobile=params['mobile'], salt=params['salt'],
                    password=params['password'],
                    created=datetime.strptime(params['created'], '%Y-%m-%d %H:%M:%S'),
                    creator=params['creator'],
                    edited=datetime.strptime(params['edited'], '%Y-%m-%d %H:%M:%S'),
                    editor=params['editor'],
                    deleted=int(params['deleted']))
        db.session.add(user)
        db.session.commit()
        return user

    def __repr__(self):
        return '<User>'


class UsersView(Resource):
    def get(self):
        data = json.dumps({
            'name': 'wd',
        })
        resp = Response(response=data, status=200, mimetype="application/json")
        return resp

    @marshal_with(my_fields)
    def post(self):
        """
        @@@
        ### args
        | args | nullable | type | remark |
        |------|----------|------|--------|
        | id   |  false   | int  |todo id |
        ### return
        - #### json
        > {......}
        @@@
        """
        if not request.values:
            abort(404)
        params = request.values.to_dict()
        user = User(state=int(params['state']),
                    name=params['name'],
                    head_img_url=params['head_img_url'],
                    mobile=params['mobile'], salt=params['salt'],
                    password=params['password'],
                    created=datetime.strptime(params['created'], '%Y-%m-%d %H:%M:%S'),
                    creator=params['creator'],
                    edited=datetime.strptime(params['edited'], '%Y-%m-%d %H:%M:%S'),
                    editor=params['editor'],
                    deleted=int(params['deleted']))
        db.session.add(user)
        db.session.commit()
        return user
