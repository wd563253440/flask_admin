# -*- coding: utf-8 -*-
"""
-----------------------------------------------
@version 3.7
@time 2021/3/25 17:53
@author passion.wangd
@title
@file user.py
@IDE PyCharm
-----------------------------------------------
"""
from app.models.db import db
'''
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '用户ID',
  `state` tinyint(1) DEFAULT NULL COMMENT '用户状态:0=正常,1=禁用',
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '姓名',
  `head_img_url` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '头像图片地址',
  `mobile` varchar(11) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '手机号码',
  `salt` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '密码加盐',
  `password` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '登录密码',
  `created` datetime DEFAULT NULL COMMENT '创建时间',
  `creator` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '创建人',
  `edited` datetime DEFAULT NULL COMMENT '修改时间',
  `editor` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '修改人',
  `deleted` tinyint(1) unsigned zerofill DEFAULT '0' COMMENT '逻辑删除:0=未删除,1=已删除',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC COMMENT='用户';
'''
class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(1))
    name = db.Column(db.String(255))
    head_img_url = db.Column(db.String(255))
    mobile = db.Column(db.String(11))
    salt = db.Column(db.String(64))
    password = db.Column(db.String(64))
    created = db.Column(db.Date)
    creator = db.Column(db.String(64))
    edited = db.Column(db.Date)
    editor = db.Column(db.String(64))
    deleted = db.Column(db.String(1))
