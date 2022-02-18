#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sqlite3

homework_dict = [{'姓名': '学员1', '年龄': 37, '作业数': 1},
                 {'姓名': '学员2', '年龄': 33, '作业数': 5},
                 {'姓名': '学员3', '年龄': 32, '作业数': 10}]

# 连接SQLite 数据库
conn = sqlite3.connect('homework_dict.sqlite')
cursor = conn.cursor()

# 执行创建表的任务

# cursor.execute("create table homework_info(姓名 varchar(40),年龄 int,作业数 int)")
#cursor.execute("insert into homework_info('姓名','年龄','作业数') values ('学员1',37,1)")



# 读取Python 字典数据，并逐条写入SQLite数据库
for teacher in homework_dict:
    name = teacher['姓名']
    age = teacher['年龄']
    homework = teacher['作业数']

    cursor.execute("insert into homework_info('姓名','年龄','作业数') values (print(name),print(age),print(homework))")
    #cursor.execute("insert into homework_info('姓名','年龄','作业数') values ('学员3',32,10)")


    #cursor.execute("select * from qytang_homework_info")
    #print(teacher)
conn.commit()