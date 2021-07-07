#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-
import os
import re

os.chdir('/home/centos/test')

print('文件中包含“qytang”关键字的文件为：')
print('方案一:')
for file_or_dir in os.listdir(os.getcwd()):
    #匹配file的文件，并且文件中含有'qytang'关键字的
    if os.path.isfile(file_or_dir) and 'qytang' in open(file_or_dir,'r').read():
        print(file_or_dir)


# 这是更优化的递归方案
# topdown的作用
# True从主目录扫描到子目录
# False从子目录扫描到主目录

print('方案二:')
for root, dirs, files in os.walk(os.getcwd(), topdown=False):
    for name in files:
        #files结果为list，所以用for循环迭代，然后用name迭代匹配'qytang'
        if 'qytang' in open(name,'r').read():
            print(name)

#完成清理工作

os.chdir('..')
for root, dirs, files in os.walk('test', topdown=False):
    for name in files:
        os.remove(os.path.join(root, name))
    for name in dirs:
        os.rmdir(os.path.join(root, name))

os.removedirs('test')
