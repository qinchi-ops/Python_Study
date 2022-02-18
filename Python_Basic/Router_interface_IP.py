#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-
from ssh import centos_ssh
from ping import centos_ping
import re
import pprint

#def router_get_if(*ips,username='admin',password='Cisco123'):
def router_get_if(*ips,username,key_filename):
    device_if_dict = {}
    while True:

        if ips in centos_ping:
            centos_ssh(*ips,username,key_filename,cmd='pwd/ \n ls')
        return device_if_dict
    else:



if __name__ == "__main__":
    #pprint.pprint(router_get_if('192.168.1.1','192.168.1.2',username='admin',password='Cisco123'),indent=4)
    pprint.pprint(router_get_if('172.31.37.202','centos', '/home/centos/ssh_keys/Centos7.pem'), indent=4)
    #print(router_get_if('172.31.37.202','centos', '/home/centos/ssh_keys/Centos7.pem')



