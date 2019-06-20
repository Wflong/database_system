#!/usr/bin/python
# -*- coding:utf-8 -*-
from bin.db_commands.tb_control.operation_tbs import Table
from bin.untils.tools import error_command


tb_oper = Table()

def tboper(oper):
    """
    处理数据库操作函数
    :return:
    """
    contro_lst = oper.split(" ")
    try:
        op = contro_lst[0]
    except Exception:
        error_command()

    try:
        if op == 'create':
            tb_name = contro_lst[2]
            date = contro_lst[3]
            tb_oper.create_table(tb_name, date)
        elif op == 'show':
            tb_oper.show_tables()
        elif op == 'drop':
            tb_name = contro_lst[2]
            tb_oper.drop_table(tb_name)
        elif op == 'alter':
            old_name = contro_lst[3]
            o = contro_lst[2]
            new_name = contro_lst[4]
            tb_oper.rename_table(old_name, new_name)
        elif op == 'insert':
            date = contro_lst[4]
            tb_name = contro_lst[2]
            tb_oper.insert_date(date, tb_name)
        elif op == 'select':
            tag = contro_lst[1]
            tb_name = contro_lst[-1]
            tb_oper.select_date(tag, tb_name)
        elif op == 'delete':
            tb_name = contro_lst[2]
            tag = contro_lst[4]
            tb_oper.delete_data(tag, tb_name)
        elif op == 'update':
            tb_name = contro_lst[1]
            value = contro_lst[3]
            section = contro_lst[5]
            tb_oper.update_data(tb_name, value, section)
        else:
            error_command()
    except Exception as e:
        error_command()
        print e
