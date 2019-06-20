#!/usr/bin/python
# -*- coding:utf-8 -*-
from bin.db_commands.tb_control.tb_handler import tboper
from bin.untils.tools import my_help, error_command
from bin.db_commands.db_control.db_handler import dboper


def sql_analysis(oper):
    """
    用户命令解析器,若对数据库操作，则交给数据库处理视图，反之交给数据表操作视图
    :param oper: 输入的命令
    :return:
    """
    database_oper_lst = ['database', 'databases', 'database()']
    tables_oper_lst   = ['tables', 'table', 'insert', 'delete', 'update']
    try:
        oper_tag = oper.split(" ")[1]
    except Exception:
        if oper == '--help':
            my_help()
        else:
            error_command()
    else:
        if oper_tag in database_oper_lst or 'use' in oper:
            dboper(oper)
        elif oper_tag in tables_oper_lst or 'insert' in oper or 'from' in oper or 'update' in oper:
            tboper(oper)
        else:
            error_command()
