#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import shutil

from bin.untils.tools import change_db, get_dbname, is_exists, ui
from config.public_path import DATABASE_PATH


class Database(object):
    """
    数据库操作类，主要处理对数据据操作的而逻辑
    """
    def __init__(self):
        pass

    def create_db(self, db_name):
        """
        创建数据库，并且还到该数据库
        :param db_name: 数据库名
        :return:
        """
        try:
            os.mkdir(DATABASE_PATH + db_name)
        except Exception as e:
            print "The db:%s has been existed!"%db_name
        print "Create database : %s ssuccessfully"%db_name

    def use_db(self, db_name):
        """
        切换数据库，如果没有该数据库则创建，有则切换
        :param db_name: 数据库名字
        :return:
        """
        if is_exists(db_name, "db"):
            pass
        else:
            self.create_db(db_name)
        change_db(db_name)
        print "Switch to database: %s!" % db_name

    def drop_db(self, db_name):
        """
        删除数据库
        :param db_name: 要删除的数据库名
        :return:
        """
        try:
            shutil.rmtree(DATABASE_PATH + "%s"%db_name)
            print "The database %s delete successfully!"%db_name
        except Exception as e:
            print "The database %s is not existed!"%db_name

    def rename_db(self, old_name, new_name):
        """
        重命名数据库
        :param old_name: 旧的数据空间名
        :param new_name: 更新后的数据库名
        :return:
        """
        try:
            os.rename(DATABASE_PATH + old_name, DATABASE_PATH + new_name)
            change_db(new_name)
            print "The database %s rename successfully!"%old_name
        except Exception as e:
            print "The database %s rename failded!"%old_name

    def show_dbs(self):
        """
        显示所有的数据库
        :return:
        """
        dbs =  os.listdir(DATABASE_PATH)
        ui('dbs', dbs)

    def current_db(self):
        """
        显示当前使用的数据库
        :return:
        """
        current_db_name = get_dbname()
        print 'current database:%s'%current_db_name

