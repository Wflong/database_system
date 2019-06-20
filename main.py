#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys

from bin.db_commands.handler import sql_analysis
from bin.untils.tools import change_db, get_dbname

sys.path.extend(
      [
          '/opt/gsql/config',
          '/opt/gsql/bin/db_commands',
          '/opt/gsql/bin/data_structure',
          '/opt/gsql/bin/untils',
       ]
   )
reload(sys)


import getopt
import getpass

from def_auth import *


options = """Options:
                  -U <username>,     input your username
                  -p <password>,     input your password
                  --help             show help info       
             """


def auth(username, password):
    """
    用户校验函数
    :param username: 用户名
    :param password: 密码
    :return:
    """
    if username == USER_NAME and password == PASSWORD:
        return True
    else:
        return False


def login(argv):
    """
    登陆系统
    :return:
    """
    username = ''
    password = ''

    try:
        opts, args = getopt.getopt(argv, 'U:h:p:d', ['help'])
    except getopt.GetoptError:
        print options
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h' or opt == '--help':
            print options
        elif opt == '-U':
            username = arg
        elif opt == '-p':
            password = arg
        else:
            print options

    if not username:
        username = raw_input('Please input your username: \n>')
    if not password:
        password = getpass.getpass('Please input the %s password: \n>'%username)

    return auth(username, password)


def operation():
    """
    系统操作入口函数
    :return:
    """
    while True:
        oper = raw_input('%s#> '%get_dbname())
        if oper == 'exit':
            change_db("")
            print 'Bye~'
            sys.exit()
        else:
            sql_analysis(oper)



def main():
    if login(sys.argv[1:]):
        operation()
    else:
        print 'username or password error!'


if __name__ == '__main__':
    main()

