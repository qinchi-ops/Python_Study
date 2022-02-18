#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-

import logging
#  关闭不必要的报错
logging.getLogger('kamene.runtime').setLevel(logging.ERROR)

from kamene.all import *
from kamene.layers.inet import ICMP, IP

def centos_ping(*ip):
    # 构建ping数据包

    # Ping并且把返回结果赋值给ping_result
    for x in ip:
        ping_pkt = IP(dst=ip) / ICMP()
        print(x)
        # ping_result = sr1(ping_pkt, timeout=2, verbose=False)
        # if ping_result :
        # # 设计返回值
        #     return (x+' 通!')
        # #return ips
        # else:
        #     return (x+' 不通!')

if __name__ == '__main__':
    result = centos_ping('1.1.1.1','2.2.2.2')
    #result2 = centos_ping('8.8.8.8')
    # 根据返回值涉设计打印
    print(result)
    #print(result2)