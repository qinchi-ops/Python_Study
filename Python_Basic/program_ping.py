#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-

import logging
#  关闭不必要的报错
logging.getLogger('kamene.runtime').setLevel(logging.ERROR)

from kamene.all import *
from kamene.layers.inet import ICMP, IP

class Ping:
    def __init__(self,dst_ip):
        self.dst_ip=dst_ip
        self.size = 100

    def one(self):
        ping_pkt = IP(dst=self.dst_ip) / ICMP()
        ping_result = sr1(ping_pkt, timeout=2, verbose=False)
        if ping_result:
            print (self.dst_ip+' 可达！')
        else:
            print (self.dst_ip+' 不可达！')

    def ping(self):
         #for x in self.dst_ip:
            ping_pkt = IP(dst=self.dst_ip) / ICMP()
            ping_result = (sr1(ping_pkt, timeout=2, verbose=False))*5
            if 5*ping_result:
                print (5*'!')
            else:
                print (5*'.')
    def length(self,size):
        self.size= 200

    def srcip(self,src_ip):
        # for x in self.dst_ip:
        self.src_ip=src_ip
        ping_pkt = IP(src=self.src_ip,dst=self.dst_ip) / ICMP()
        ping_result = (sr1(ping_pkt, timeout=2, verbose=False))*5
        if 5*ping_result:
            print (5*'!')
        else:
            print (5*'.')

    def __str__(self):
        return f'<{self.__class__.__name__} =>  dstip: {self.dst_ip} , size: {self.size} >'

class NewPing(Ping):
        def ping(self):
        # for x in self.dst_ip:
            ping_pkt = IP(dst=self.dst_ip) / ICMP()
            ping_result = (sr1(ping_pkt, timeout=2, verbose=False))*5
            if 5*ping_result:
                print (5*'+')
            else:
                print (5*'?')

if __name__ == '__main__':
    ping = Ping('1.1.1.1')
    total_len = 70
    def print_new(word, s='-'):
        print('{0}{1}{2}'.format(s*int((70-len(word))/2), word, s * int((70 - len(word))/2)))
    print_new('print class')
    print(ping)
    print_new('print one for sure reachable')
    ping.one()  # Ping一个包判断可达性
    print_new('ping five')
    ping.ping()  # 模拟正常ping程序ping五个包,'!'表示通,'.'表示不通
    print_new('set payload lenth')
    ping.length = 200  # 设置负载长度
    print(ping)  # 打印类
    ping.ping()  # 使用修改长度的包进行Ping测试
    print_new('set ping src ip address')
    ping.srcip = '192.168.1.123'  # 修改源IP地址
    print(ping)  # 打印类
    print_new('new class NewPing', '=')
    newping = NewPing('8.8.8.8')  # 使用新的类NewPing（通过继承QYTANG类产生）产生实例
    newping.length = 300
    print(newping)  # 打印类
    newping.ping()  # 打印Newping类自定义过ping()这个方法，'+'表示通，'?'表示不通