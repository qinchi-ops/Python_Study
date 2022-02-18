#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from kamene import *
from kamene.layers.inet import ICMP, IP, sr1
import logging

#  关闭不必要的报错
logging.getLogger('kamene.runtime').setLevel(logging.ERROR)


class QYTPING:
    def __init__(self, ip):
        self.ip = ip
        self.length = 100
        self.srcip = ''

    def make_pkt(self):
        if self.srcip:
            self.pkt = IP(src=self.srcip,dst=self.ip) / ICMP() / (b'v' * self.length)
        else:
            self.pkt = IP(dst=self.ip) / ICMP() / (b'v' * self.length)

    def one(self):
        self.make_pkt()
        result = sr1(self.pkt, timeout=2, verbose=False)
        if result:
            print(self.ip, '可达!')
        else:
            print(self.ip, '不可达！')

    def ping(self):
        self.make_pkt()
        for i in range(5):
            result = sr1(self.pkt, timeout=2, verbose=False)
            if result:
                print('!', end='', flush=True)
            else:
                print('.', end='', flush=True)
        print()

    def __str__(self):
        if not self.srcip:
            return '<{0} => dstip:  {1}, size:  {2}>'.format(self.__class__.__name__, self.ip, self.length)
        else:
            return '<{0} => srcip: {1}, dstip:  {2}, size:  {3}>'.format(self.__class__.__name__, self.srcip, self.ip,self.length)


class NewPing(QYTPING):
    def ping(self):
        self.make_pkt()
        for i in range(5):
            result = sr1(self.pkt, timeout=1, verbose=False)
            if result:
                print('+', end='', flush=True)
            else:
                print('?', end='', flush=True)
        print()


if __name__ == '__main__':
    ping = QYTPING('1.1.1.1')  # 使用类QYTPING，产生实例
    total_len = 70

    def print_new(word, s='-'):
        print('{0}{1}{2}'.format(s * int((70 - len(word)) / 2), word, s * int((70 - len(word)) / 2)))


    print_new('print class')
    print(ping)  # 打印类
    print_new('print one for sure reachable')
    # Ping一个包判断可达性
    ping.one()
    print_new('ping five')
    ping.ping()  # 模拟正常ping程序ping五个包,'!'表示通,'.'表示不通
    print_new('set payload lenth')
    ping.length = 200  # 设置负载长度
    print(ping)  # 打印类
    ping.ping()  # 使用修改长度的包进行Ping测试
    print_new('set ping src ip address')
    ping.srcip = '192.168.1.123'  # 修改源IP地址
    print(ping)  # 打印类
    ping.ping()
    print_new('new class NewPing', '=')
    newping = NewPing('192.168.1.1')  # 使用新的类NewPing（通过继承QYTANG类产生）产生实例
    newping.length = 300
    print(newping)  # 打印类
    newping.ping()  # 打印Newping类自定义过ping()这个方法，'+'表示通，'?'表示不通
