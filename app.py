# -*- coding: utf-8 -*-
"""
-----------------------------------------------
@version 3.7
@time 2021/3/12 17:43
@author passion.wangd
@title
@file app.py
@IDE PyCharm
-----------------------------------------------
"""
from flask import Flask
from flask_cors import CORS

web_app = Flask(
    __name__,
    template_folder='../template/',
    static_folder='../static/'
)

@web_app.route('/', methods=['GET', 'POST'], endpoint='index')
def index():
    return '项目启动'

if __name__ == '__main__':
    web_app.run(host='127.0.0.1',debug=True)
