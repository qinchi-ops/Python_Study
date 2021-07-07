#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-

import logging
#  关闭不必要的报错
logging.getLogger('kamene.runtime').setLevel(logging.ERROR)

from kamene.all import *
from kamene.layers.inet import ICMP, IP

def qytang_ping(ip):
    # 构建ping数据包
    ping_pkt = IP(dst=ip)/ICMP()
    # Ping并且把返回结果赋值给ping_result
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result :
        # 设计返回值
        return (ip+' 通!')
    else:
        return (ip+' 不通!')

if __name__ == '__main__':
    result = qytang_ping('1.1.1.1')
    result2 = qytang_ping('196.21.5.254')
    # 根据返回值涉设计打印
    print(result)
    print(result2)
