#!/usr/bin/python
# -*- coding:utf-8 -*-
import os

from bin.data_structure.tree import Tree
from bin.untils.tools import get_dbname, ui, get_date
from config.public_path import DATABASE_PATH


class Table():
    """
    对table操作的封装
    """
    def __init__(self):
        pass

    def __check_db(self):
        """
        对数据表操作之前必须选定一个数据库
        :return:
        """
        if not get_dbname():
            print 'Please select a database!'
            return False
        return True

    def __write_date(self, tb_path, date, tb_name):

        try:
            f1 = open(tb_path, 'rb')
            f2 = open(tb_path, 'aw')
            lst = f1.readlines()
            i = len(lst)
            dates = get_date(date, str(i + 1))
            f2.write(dates)
            # 将表中的数据存储到树中，ID为索引
            t = Tree()
            t.add(i + 1, dates.strip('\n'))
        except Exception as e:
            print 'error', e
        else:
            f1.close()
            f2.close()
        print 'insert into %s succefully!'%tb_name

    def create_table(self, tb_name, date):
        """
        创建数据表
        :param tb_name:
        :return:
        """
        # 创建用于存储表中数据的磁盘文件
        if self.__check_db():
            try:
                os.mknod(DATABASE_PATH + "%s/%s"%(get_dbname(), tb_name + '.txt'))
                print "Create table %s successfully!"%tb_name
            except Exception as e:
                print "The table:%s has been existed!"%tb_name
            # 创建一张表就会创建一棵树，树的名字就是表的名字
            tb_path = DATABASE_PATH + "%s/%s"%(get_dbname(), tb_name + '.txt')
            self.__write_date(tb_path, date, tb_name)

    def drop_table(self, tb_name):
        """
        删除表
        :param tb_name: 表名
        :return:
        """
        if self.__check_db():
            try:
                os.remove(DATABASE_PATH + get_dbname() + "/%s.txt"%tb_name)
                print "The tables %s delete successfully!"%tb_name
            except Exception as e:
                print e
                print "The tables %s is not existed!"%tb_name

    def rename_table(self, tb_name, new_name):
        """
        更改表名
        :param tb_name: 原来的表名
        :param new_name: 新表名
        :return:
        """
        if self.__check_db():
            path = DATABASE_PATH + get_dbname() + "/"
            try:
                os.rename(path + tb_name + '.txt', path + new_name + '.txt')
                print "The table %s rename successfully!"%tb_name
            except Exception as e:
                print e
                print "The table %s rename failded!"%tb_name

    def show_tables(self):
        """
        显示当前操作数据库下的所有表
        :return:
        """

        if self.__check_db():
            tbs_lst = []
            tbs = os.listdir(DATABASE_PATH + get_dbname())
            for t in tbs:
                tbs_lst.append(t.split('.')[0])
            ui('tbs', tbs_lst)

    def insert_date(self, date, tb_name):
        """
        插入数据，使用方法：insert into tb_name value (xxx=xxx,xxx=xxx)
        :param tb_name: 要插入的表的名字
        :param date: 要插入的数据
        :return:
        """
        tb_path = DATABASE_PATH + "%s/%s" % (get_dbname(), tb_name + '.txt')
        self.__write_date(tb_path, date, tb_name)

    def select_date(self, tag, tb_name):
        """
        数据库查询操作
        select * from tb_name    查询该数据表中所有记录
        select count(*) from tb_name 查询该表中的总记录数量
        :param tag: * or count(*)
        :param tb_name: 表名
        todo!加where 条件查询，只要加where就会用到索引树
        :return:
        """
        tb_path = DATABASE_PATH + "%s/%s" % (get_dbname(), tb_name + '.txt')
        with open(tb_path, 'r') as f:
            res = f.readlines()
        if tag == '*':
            print '----------------------datas--------------------------'
            for r in res:
                print r.strip('\n')
            print '-----------------------------------------------------'
        elif tag == 'count(*)':
            print 'count: ', len(res)

    def delete_data(self, tag, tb_name):
        """
        删除数据库中的符合指定条件的记录
        :param tag: 字段
        :param value: 值
        用法：delete from tb_name where xx=xx
        :return:
        """
        result = []

        tb_path = DATABASE_PATH + "%s/%s" % (get_dbname(), tb_name + '.txt')
        with open(tb_path, 'r') as f:
            res = f.readlines()

        for r in res:
            raw = r.strip('\n')
            li_raw = raw.replace('\t', ',')
            li_lst = li_raw.split(',')
            if tag not in li_lst:
                result.append(r)

        with open(tb_path, 'w') as f:
            f.writelines(result)

        if len(res) == len(result):
            print 'The data is not exist!'
        else:
            print 'Delete data successfully!'

    def update_data(self, tb_name, value, section):
        """
        更新记录操作
        用法：update tb_name set xx=xx where id=?
        :return:
        """
        tb_path = DATABASE_PATH + "%s/%s" % (get_dbname(), tb_name + '.txt')
        with open(tb_path, 'r') as f:
            res = f.readlines()

        tag = value.split('=')[0]

        flag = False
        update_set = []

        for r in res:
            raw = r.strip('\n')
            li_raw = raw.replace('\t', ',')
            li_lst = li_raw.split(',')

            if section in li_lst:
                flag = True
                new = []
                for i in li_lst:
                    if i.startswith(tag):
                        new.append(value)
                    else:
                        new.append(i)
                new_str = ','.join(new)
                new_raw = new_str.replace(',', '\t') + '\n'
                update_set.append(new_raw)
            else:
                update_set.append(r)

        if not flag:
            print 'error update,the name is not in this data!'

        with open(tb_path, 'w') as f:
            f.writelines(update_set)

        print 'update data successfully!'












