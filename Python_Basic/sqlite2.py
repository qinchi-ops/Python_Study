#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sqlite3

user_notify = """

请输入查询选项:
输入1：查询整个数据库
输入2：基于姓名查询
输入3：基于年龄查询
输入4：基于作业数查询
输入0：退出
"""

conn = sqlite3.connect('sqlite1.sqlite')
cursor = conn.cursor()
cursor.execute("select * from qytang_homework_info")


while True:
    print(user_notify)
    user_input = input('请选择:')
    if user_input == '0':
        break
    elif user_input == '1':

        yourresults = cursor.fetchall()
        for teacher in yourresults:
        ####

    elif user_input == '2':
        user_sn = input('请输入学员姓名:')
        if not user_sn:
            continue

        ###
        if not yourresults:
            print('学员信息未找到!')
        for teacher in yourresults:
    #####
    elif user_input == '3':
        user_age = input('搜索大于输入年龄的学员，请输入学员的年龄:')
        if not user_age:
            continue
        #####
        if not yourresults:
            print('学员信息未找到！')
        for teacher in yourresults:
    ####
    elif user_input == '4':
        user_homework = input('搜索大于输入作业数的学员，请输入作业数量:')
        if not user_homework:
            continue
        ####
        if not yourresults:
            print('学员信息未找到！')

        for teacher in yourresults:
    ######
    else:
        print('输入错误！请重试')