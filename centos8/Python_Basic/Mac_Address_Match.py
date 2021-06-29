#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-
#字符串为MAC地址表内容: '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'

import re   #导入regular expression
str1= '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'
result = re.match('(\d{1,4})\s+(\w{4}\.\w{4}\.\w{4})\s+(DYNAMIC|STATIC)\s+([A-Z][a-z]\d\/\d\/\d\d)',str1).groups()
#正则表达式抓取出需要的信息

string_format = '{:<15}: {}'        #定义format格式

str1 = string_format.format ('VLAN ID',result[0])
str2 = string_format.format ('MAC',result[1])
str3 = string_format.format ('Type',result[2])
str4 = string_format.format ('Interface',result[3])

max_len=max(len(str1),len(str2),len(str3),len(str4))    #计算最大行的长度

print ('='*max_len)
print (str1)
print (str2)
print (str3)
print (str4)
print ('='*max_len)
