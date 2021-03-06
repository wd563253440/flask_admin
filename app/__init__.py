# -*- coding: utf-8 -*-
"""
-----------------------------------------------
@version 3.7
@time 2021/3/25 18:16
@author passion.wangd
@title
@file __init__.py
@IDE PyCharm
-----------------------------------------------
"""
import logging
import logging.config
import yaml
import subprocess
from flask import Flask

from app.resource import api
from app.models.db import db
import common.config as config
from flask_docs import ApiDoc


def create_app(config_name=None, config_path=None):
    app = Flask(__name__,
                template_folder=subprocess.os.path.join(subprocess.os.getcwd(), '\\template\\'),
                static_folder=subprocess.os.path.join(subprocess.os.getcwd(), '\\static\\'),
                )
    app.config.from_object(config)
    db.init_app(app,)
    api.init_app(app)
    ApiDoc(app, title='接口文档', version='1.0.0')
    # 读取配置文件
    if not config_path:
        config_path = subprocess.os.path.join(subprocess.os.getcwd(), 'config\\config.yaml')
    if not config_name:
        config_name = 'PRODUCTION'
    conf = read_yaml(config_name, config_path)
    app.config.update(conf)
    if not subprocess.os.path.exists(app.config['LOGGING_PATH']):
        # 日志文件目录
        subprocess.os.mkdir(app.config['LOGGING_PATH'])
    # 日志设置
    with open(app.config['LOGGING_CONFIG_PATH'], 'r', encoding='utf-8') as f:
        dict_conf = yaml.safe_load(f.read())
    logging.config.dictConfig(dict_conf)  # 载入日志配置
    return app, api


def read_yaml(config_name, config_path):
    """
    config_name:需要读取的配置内容
    config_path:配置文件路径
    """
    if config_name and config_path:
        with open(config_path, 'r', encoding='utf-8') as f:
            conf = yaml.safe_load(f.read())
        if config_name in conf.keys():
            return conf[config_name.upper()]
        else:
            raise KeyError('未找到对应的配置信息')
    else:
        raise ValueError('请输入正确的配置名称或配置文件路径')
