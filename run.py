# -*- coding: utf-8 -*-
"""
-----------------------------------------------
@version 3.7
@time 2021/3/12 17:43
@author passion.wangd
@title
@file run.py
@IDE PyCharm
-----------------------------------------------
"""
from app import create_app
app = create_app()

app, api = create_app(config_name='DEVELOPMENT')
if __name__ == '__main__':
    app.run(host='127.0.0.1',debug=True)
