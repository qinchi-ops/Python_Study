#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-
import re       #import regular expression
import os       #import linux os command

# 执行并返回命令"route -n"的结果
route_n_result = os.popen("route -n").read()

#gateway [2] 的IP为网关，匹配
gateway = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',route_n_result)[1]

#格式化字符串并打印
string_format ='{:<5}:{}'
print(string_format.format('网关为',gateway))