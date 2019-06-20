#!/usr/bin/python
# -*- coding:utf-8 -*-
import json
import os
from config.public_path import DB_STATUS_PATH, DATABASE_PATH



def error_command():
    """
    错误命令提示
    :return:
    """
    print "Command error,input --help see help info"


def get_dbname():
    """
    获取当前数据库名字
    :return: 当前数据库名字
    """
    with open(DB_STATUS_PATH, 'r') as f:
        js = json.load(f)
        db_name = js['db_name']
        return db_name


def change_db(db_name):
    """
    改变当前数据库名称
    :param db_name:
    :return: none
    """
    with open(DB_STATUS_PATH, 'w') as f:
        json.dump({"db_name":db_name}, f)


def my_help():
    """
    帮助信息
    :return:
    """
    print """
     -----------------------------------help info-------------------------------------
     -----------------------------------for database----------------------------------
      command:                           action:
         1.use db_name                   switch database,if the database is not exist,
                                         it will create the database and switch to it. 
         2.create database db_name       create a new database
         3.drop database db_name         delete the database
         4.rename database old new_name  rename the database with new_name
         5.select database()             a function,show the current databases
         6.show databases                show all databases
     ------------------------------------for table------------------------------------
         7.create table tb_name (xx=xx,xx=xx)     create a new database and insert msg
         8.show tables                            show current database all tables
         9.drop table tb_name                     delete the table
         10.alter table rename old_name new_name  rename the database with new_name
         11.insert into tb_name  values (xx=2,xx=lisi,xx=xx)
                                                  insert a data
         12.delete from tb_name where xx=xx       delete the data
         13.update tb_name set xx=xx              update the data
         14.select * from tb_name                 search the data
         15.select count(*) from tb_name          search count of the data
     ---------------------------------------------------------------------------------

    """


def ui(type, data):
    """
    显示所有的数据库名字或者是所有的表名
    :param type: dbs:数据库  tbs:数据表
    :param data: 包含名字的列表
    :return:
    """
    print """----------List of %s----------""" % type
    for d in data:
        print d
    print """------------------------------"""


def is_exists(name, type):
    """
    判断数据库或表是否存在
    :param name: 数据库或表名字
    :param type: db代表数据库名字，tb代表表名
    :return: 存在：True 不存在：False
    """
    if type == 'db':
        return os.path.exists(DATABASE_PATH + name)
    else:
        db_name = get_dbname()
        return os.path.exists(DATABASE_PATH + "%s/%s"%(db_name, name+'.txt'))


def get_date(s, i):
    """
    获取创建表时候带的数据
    :param s:
    :return:
    """
    s_be = s[1:]
    s_en = s_be[:-2]
    ls = s_en.split(",")
    res1 = '\t'.join(ls)
    res = 'id=' + str(i) + '\t' + res1 + '\n'
    return res


