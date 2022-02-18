#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-
import re
asa_conn = "TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247,idle 0:00:00, bytes 74, flags UIO\n TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233,idle 0:00:03, bytes 334516, flags UIO"


for conn in asa_conn.split('\n'):
#re_result = re.match('\w{3}\s+\w{3,7}\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\)\s+.*',asa_conn).groups()
    re_result = re.match('\w{3}\s+\w{3,7}\s+\d{1,3}\.(\d{1,3}\.\d{1,3}\.\d{1,3})\:(\d{1,6})\s+\w{3,7}\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\:(\d{1,6})\,\w{4}\s+\d{1,2}\:\d{1,2}\:\d{1,2}\,\s+\w{5}\s+(\d{1,11})\,\s+\w{5}\s+(\w{1,5})',conn).groups()
    print(re_result)
    #print(conn)