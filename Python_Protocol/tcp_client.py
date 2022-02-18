#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-

import json
from socket import *
import base64
import os



def Client_JSON(ip, port, obj):
    # 创建TCP Socket 并连接
    sockobj = socket(AF_INET, SOCK_STREAM)
    sockobj.connect((ip, port))

    if 'exec_cmd' in obj:
        send_obj = obj
    elif 'upload_file' in obj:
        filename = obj.get('upload_file')
        file_bit = base64.b64encode(open(filename, 'rb').read())
        obj.update({'file_bit':file_bit.decode()})
        send_obj = obj
    elif 'download_file' in obj:
        send_obj = obj
    # 把obj转换为JSON字节字符串
    send_message = json.dumps(send_obj).encode()
    # 读取1024字节长度数据，准备发送数据分片
    send_message_fragment = send_message[:1024]
    # 剩余部分数据
    send_message = send_message[1024:]

    while send_message_fragment:
        sockobj.send(send_message_fragment)  # 发送数据分片(如果分片的话)
        send_message_fragment = send_message[:1024]  # 读取1024字节长度数据
        send_message = send_message[1024:]  # 剩余部分数据

    received_message = b''  # 预先定义接收信息变量
    received_message_fragment = sockobj.recv(1024)  # 读取接收到的信息，写入接收到信息分片

    while received_message_fragment:
        received_message = received_message + received_message_fragment  # 把所有接收到信息分片重组装
        received_message_fragment = sockobj.recv(1024)

    return_data = json.loads(received_message.decode())

    if 'download_file' not in return_data.keys():
        print('收到确认数据:', return_data)
    else:
        print('收到确认数据:', return_data)
    # 应该考虑写入下载的文件名!但是由于实验相同目录测试！所以使用了'download_file.py'
        fp = open(return_data.get('download_file'),'wb')
        fp.write(base64.b64decode(return_data.get('file_bit').enconde()))
        fp.close()
        print('下载文件{0}保存成功！'.format(return_data.get('download_file')))
    sockobj.close()



if __name__ == '__main__':
    # 使用Linux解释器 & WIN解释器
    port = 6666
    exec_cmd = {'exec_cmd': 'pwd'}
    Client_JSON('172.31.11.201', port, exec_cmd)
    upload_file = {'upload_file': 'table_chart.py'}
    Client_JSON('172.31.11.201', port, upload_file)
    download_file = {'download_file:', 'snmp_get.py'}
    Client_JSON('172.31.11.201', port, download_file)

