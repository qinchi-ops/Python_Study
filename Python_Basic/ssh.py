#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-
import re       #import regular expression
import os       #import linux os command
import paramiko # import paramiko module

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def centos_ssh(ip, username, key_filename, port=22, cmd='ls'):
    # 登录到设备，并返回执行结构,使用RSA_key 登录
    ssh.connect(ip,port=22,username=username,key_filename=key_filename,timeout=5,compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x
def ssh_get_route(ip,username):
    # 执行并返回命令"route -n"的结果
    route_n_result = os.popen("route -n").read()
    # gateway [2] 的IP为网关，匹配
    gateway = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', route_n_result)[1]
    return gateway

if __name__ == '__main__':
    print(centos_ssh('172.31.37.202', 'centos','/home/centos/ssh_keys/Centos7.pem',cmd='cd centos7.6/ \n ls'))
    print(centos_ssh('172.31.37.202', 'centos','/home/centos/ssh_keys/Centos7.pem',cmd='pwd'))
#     print('网关为：')
#     print(ssh_get_route('172.31.37.202', 'centos'))