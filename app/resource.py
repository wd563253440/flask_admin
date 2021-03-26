# -*- coding: utf-8 -*-
"""
-----------------------------------------------
@version 3.7
@time 2021/3/25 16:56
@author passion.wangd
@title
@file resource.py
@IDE PyCharm
-----------------------------------------------
"""
from flask_restful import Api
from flask import views
from app.api.management.user import User, Users
from app.api.management.role import Role, Roles
api = Api()
api.add_resource(User, '/api/user/<int:id>')
api.add_resource(Users, '/api/users/')
api.add_resource(Role, '/api/role/<int:id>')
api.add_resource(Roles, '/api/roles/')
