#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import datetime
from time import time

datetime.datetime().now()


from matplotlib import pyplot as plt
import matplotlib

print(matplotlib.matplotlib_fname())
# 设置中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family'] = 'sans-serif'


def mat_bing(size_list, name_list):
    # 调节图形大小，宽，高
    plt.figure(figsize=(6, 6))

    # 将某部分爆炸出来，使用括号，将第一块分割出来的与其他两块的间隙
    # explode = (0.01,0.01,0.01,0.01)

    patches, label_text, percent_text = plt.pie(size_list,
                                                # explode=explode,
                                                labels=name_list,
                                                autopct='%3.1f%%',
                                                shadow=False,
                                                startangle=90,
                                                pctdistance=0.6)

    for l in label_text:
        l.set_size = 30
    for p in percent_text:
        p.set_size = 20

    plt.axis('equal')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    counters = [30, 53, 12, 45]
    protocols = ['http协议', 'ftp协议', 'rdp协议', 'qq协议']
    mat_bing(counters, protocols)
