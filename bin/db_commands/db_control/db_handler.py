#!/usr/bin/python
# -*- coding:utf-8 -*-
from bin.db_commands.db_control.operation_dbs import Database
from bin.untils.tools import error_command

db_oper = Database()

def handler(oper):
    """
    针对数据库操作命令进行解析
    :param oper:
    :return:
    """
    contro_lst = oper.split(" ")
    return contro_lst


def dboper(oper):
    """
        处理数据库操作函数
        :return:
        """
    contro_lst = handler(oper)
    try:
        op = contro_lst[0]
    except Exception:
        error_command()

    if op == 'use':
        db_name = contro_lst[1]
        db_oper.use_db(db_name)
    elif op == 'create':
        db_name = contro_lst[2]
        db_oper.create_db(db_name)
    elif op == 'drop':
        db_name = contro_lst[2]
        db_oper.drop_db(db_name)
    elif op == 'rename':
        old_name = contro_lst[2]
        new_name = contro_lst[3]
        db_oper.rename_db(old_name, new_name)
    elif op == 'show':
        db_oper.show_dbs()
    elif op == 'select':
        db_oper.current_db()
    else:
        error_command()