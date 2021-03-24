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
from app.factory import app

@app.route('/', methods=['GET', 'POST'], endpoint='index')
def index():
    app.logger.info('successfully')
    return 'successfully'

if __name__ == '__main__':
    app.run(host='127.0.0.1',debug=True)
