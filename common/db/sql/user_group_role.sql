/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 80022
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 80022
File Encoding         : 65001

Date: 2021-03-25 16:20:47
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for user_group_role
-- ----------------------------
DROP TABLE IF EXISTS `user_group_role`;
CREATE TABLE `user_group_role` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `user_group_id` bigint DEFAULT NULL COMMENT '用户组ID',
  `role_id` bigint DEFAULT NULL COMMENT '角色ID',
  `created` datetime DEFAULT NULL COMMENT '创建时间',
  `creator` varchar(36) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '创建人',
  `edited` datetime DEFAULT NULL COMMENT '修改时间',
  `editor` varchar(36) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '修改人',
  `deleted` tinyint(1) unsigned zerofill DEFAULT '0' COMMENT '逻辑删除:0=未删除,1=已删除',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `member_group_id` (`user_group_id`) USING BTREE COMMENT '用户组ID',
  KEY `role_id` (`role_id`) USING BTREE COMMENT '角色ID',
  CONSTRAINT `user_group_role_ibfk_1` FOREIGN KEY (`user_group_id`) REFERENCES `user_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `user_group_role_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC COMMENT='用户组角色';
