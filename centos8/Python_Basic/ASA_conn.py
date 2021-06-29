#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-

import re  #import regular expression
str1 = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'

result = re.match('(TCP|UDP)\s+[a-z]{6}\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\:\d{1,5})\s+\w{11}\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\:\d{1,5})\,\s+idle\s+(\d{1,2}\:\d{1,2}\:\d{1,2})\,\s+bytes\s+(\d{1,10})\,\s+flags\s+([A-Z]{3})',str1).groups()
#正则表达式抓取出需要的信息

string_format = '{:<15}: {}'    #定义字符串格式化
str1 = string_format.format('prococol',result[0])
str2 = string_format.format('server',result[1])
str3 = string_format.format('localserver',result[2])
str5 = string_format.format('bytes',result[4])
str6 = string_format.format('flags',result[5])
#str4 = string_format.format('idle',result[3])

a = result[3]
b =  a.split(':')   #切片
date_format = '{:<15}: {}小时{}分钟{}秒' #对时间单独格式化
str4 = date_format.format('idle',b[0],b[1],b[2])

max_len=max(len(str1),len(str2),len(str3),len(str4),len(str5),len(str6))    #计算最大行的长度

print('='*max_len)
print(str1)
print(str2)
print(str3)
print(str4)
print(str5)
print(str6)
print('='*max_len)