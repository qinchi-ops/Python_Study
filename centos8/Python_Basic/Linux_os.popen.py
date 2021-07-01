#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-
import os   #import os
import re   #import regular expression

#获取linux  etho网卡的信息“ifconfig eth0”
ifconfig_result = os.popen('ifconfig '+ 'eth0').read()

#赋值并提取需要数据
ipv4_add = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ifconfig_result)[0]
netmask = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ifconfig_result)[1]
broadcast = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ifconfig_result)[2]
mac_addr = re.findall('[a-z0-9]{2}\:[a-z0-9]{2}\:[a-z0-9]{2}\:[a-z0-9]{2}\:[a-z0-9]{2}\:[a-z0-9]{2}',ifconfig_result)[0]

#格式化字符换
string_format = '{:<10}: {}'

#打印结果
print(string_format.format('ipv4_add',ipv4_add))
print(string_format.format('netmask',netmask))
print(string_format.format('broadcast',broadcast))
print(string_format.format('mac_addr',mac_addr))

#产生网关的IP

#第一种方法，将IP地址最后一位替换成为“254”
# c=ipv4_add.split('.')
# c[3]='254'
# ipv4_gw ='.'.join(c)

#将IP地址最后替换为真实网关（AWS EC2的原因）
ipv4_gw  = re.sub('11.201','0.1',ipv4_add)

#打印网关的IP
print ('\n我们网关IP地址为最后一位不是254，因为网关IP地址为：' + ipv4_gw + '\n')

#Ping网关
ping_result = os.popen('ping '  + ipv4_gw+ ' -c 1 ').read()   #ping网关地址

#使用正则表达式匹配结果
re_ping_result =  re.findall('\d{1,5}\s+bytes\s+from\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ping_result)[0]

if re_ping_result:
    print('网关可达！')
else:
    print('网关不可达！')

