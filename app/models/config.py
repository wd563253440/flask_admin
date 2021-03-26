# -*- coding: utf-8 -*-
"""
-----------------------------------------------
@version 3.7
@time 2021/3/26 11:15
@author passion.wangd
@title
@file config.py
@IDE PyCharm
-----------------------------------------------
"""
# DIALECT = 'mysql'
# DRIVER = 'pymysql'
# USERNAME = 'root'
# PASSWORD = '123456'
# HOST = '127.0.0.1'
# PORT = '3306'
# DATABASE = 'test'

# SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT,
#                                                                        DATABASE)
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/test?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False
# 本地加载
# app.config['API_DOC_CDN'] = False

# 禁用文档页面
# app.config['API_DOC_ENABLE'] = False

# 需要显示文档的 Api
API_DOC_MEMBER = ['api', 'platform']

# 需要排除的 RESTful Api 文档
# app.config['RESTFUL_API_DOC_EXCLUDE'] = []