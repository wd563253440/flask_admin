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
from app.api.management.user import UserView, UsersView
from app.api.management.role import Role, Roles
api = Api()
api.add_resource(UserView, '/api/user/<int:id>')
api.add_resource(UsersView, '/api/users')
api.add_resource(Role, '/api/role/<int:id>')
api.add_resource(Roles, '/api/roles/')
