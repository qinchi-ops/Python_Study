#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-

#第五个作业有点迷糊，照着视频抄的

import re   #导入regular expression

str1='Port-channel1.189				192.168.189.254			YES			CONFIG		up '
result=re.match ('([A-Z]\S+\d)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\w+\s+\w+\s+(up|down)',str1).groups()
#匹配抓取接口信息，IP地址及状态数据

string_format='{:<10}：{}'           #格式化

str1 = string_format.format('接口',result[0])
str2 = string_format.format('IP地址',result[1])
str3 = string_format.format('状态',result[2])

max_len = max (len(str1),len(str2),len(str3))

print('='*max_len)
print(str1)
print(str2)
print(str3)
print('='*max_len)
