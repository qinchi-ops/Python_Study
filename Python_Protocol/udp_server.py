#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import socket
import sys
import pickle
import hashlib
import struct


address = ("0.0.0.0", 6666)
# 创建UDP套接字Socket, AF_INET为IPv4, SOCK_DGRAM为Datagram就是UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 套接字绑定到地址,元组(host, port)
s.bind(address)

print('UDP服务器就绪！等待客户数据！')
while True:

    try:
        recv_source_data = s.recvfrom(2048)
        rdata, addr = recv_source_data
        udp_header = rdata[:12]  # 获取udp头部信息
        uppack_header = struct.unpack('>HHLL', udp_header)  # 解包 udp头部
        version = uppack_header[0]
        pkt_type = uppack_header[1]
        seq_id = uppack_header[2]
        length = uppack_header[3]

        rdata = rdata[12:]
        data = rdata[:length]
        md5_recv = rdata[length:]

        m = hashlib.md5()
        m.update(udp_header + data)
        md5_value = m.digest()

        #if md5_recv == md5_value.encode():
        if md5_recv == md5_value:
            print('=' * 80)
            print("{0:<30}:{1:<30}".format("数据来自于", str(addr)))
            print("{0:<30}:{1:<30}".format("数据序号为", seq_id))
            print("{0:<30}:{1:<30}".format("数据长度为", length))
            print("{0:<30}:{1:<30}".format("数据内容为", str(pickle.loads(data))))

    except KeyboardInterrupt:
        sys.exit()
