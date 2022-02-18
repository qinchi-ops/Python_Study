#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import socket
import pickle
import struct
import hashlib

def udp_send_data(ip, port, data_list):
    address = (ip, port)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    version = 1
    pkt_type = 1
    seq_id = 1
    for x in data_list:
        # -----header 设计---
        # 2 字节 版本 1
        # 2 字节 类型 1 为请求 2 为响应(由于是UDP单向流量!所有此次试验只有请求)
        # 4 字节 ID号
        # 4 字节 长度

        # ---变长数据部分---
        # 使用pickle转换数据

        # ---HASH校验---
        # 16 字节 MD5值

        send_data = pickle.dumps(x)
        length = len(send_data)
        udp_header = struct.pack('>HHLL', version, pkt_type, seq_id,length)
        m = hashlib.md5()
        m.update(udp_header + send_data)
        md5_value = m.digest()
        s.sendto(udp_header+send_data+md5_value,address)
        seq_id += 1

    s.close()

if __name__ == "__main__":
    user_data = ['乾颐堂', [1, 'qytang', 3], {'qytang': 1, 'test': 3}]
    udp_send_data('172.31.11.201', 6666, user_data)