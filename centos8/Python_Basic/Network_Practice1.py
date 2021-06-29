#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-


ip = input ('请输入要查询的IP地址：')
ip_list = ip.split('.')

print ('该IP地址属于' + ip_list[2] + '楼。')
