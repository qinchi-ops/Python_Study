#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-
import re  #import regular expression

asa_conn = "TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247,idle 0:00:00, bytes 74, flags UIO\nTCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233,idle 0:00:03, bytes 334516, flags UIO"
asa_dict = {}

for conn in asa_conn.split('\n'):
    re_result = re.match('\w{3}\s+\w{3,7}\s+\d{1,3}\.(\d{1,3}\.\d{1,3}\.\d{1,3})\:(\d{1,6})\s+\w{3,7}\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\:(\d{1,6})\,\w{4}\s+\d{1,2}\:\d{1,2}\:\d{1,2}\,\s+\w{5}\s+(\d{1,11})\,\s+\w{5}\s+(\w{1,5})',str(conn)).groups()
    #print(re_result[0:4])      "测试"
    #print(re_result[4:6])      “测试”
    #将re.match的数据键值到dict
    asa_dict[re_result[0:4]]  = re_result[4:6]

print ('打印分析后的字典!\n')
print (asa_dict)

print ('\n格式化打印输出\n')

#格式化字符串
format_str1= '{:^8}:{:<11}| {:<8}:{:^10}|{:^8}:{:^15}|{:^10}:{:^10}'
format_str2 ='{:^8}:{:^11}| {:<8}:{:^10}'

for key,value in asa_dict.items():
        #key,value循环，对应位置来填充
        print(format_str1.format('src_ip',key[0],'src_port',key[1],'dst_ip',key[2],'dst_port',key[3]))
        print(format_str2.format('bytes',value[0],'flags',value[1]))
        #计算最长的长度
        print('='*len(format_str1.format('src_ip',key[0],'src_port',key[1],'dst_ip',key[2],'dst_port',key[3])))

