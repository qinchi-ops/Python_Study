#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-

import os #import linux os command
import re #import regular expression
import time #import linux time.sleep()

while True:
    #使用'netstat -tulnp'命令查询服务器上端口服务
    result = os.popen('netstat ' + '-tulnp').read()
    #匹配抓取端口号
    http_port = re.findall('tcp\s+\d\s+\d\s+0.0.0.0\:(\d{1,6})', result)
    #判断80是否在http_port中
    if '80' in http_port:
        print('HTTP TCP/80服务已打开')
        break
    else:
        time.sleep(3)
    print('等待三秒秒开始重新监控!')