#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import datetime

fivedayago=(datetime.datetime.now()-datetime.timedelta(days = 5))
now=datetime.datetime.now()
# print(now.strftime('%Y-%m-%d %H:%M:%S'))
# print(fivedayago.strftime('%Y-%m-%d %H:%M:%S'))

file = open('save_fivedayago_time_'+str(now.strftime('%Y-%m-%d %H:%M:%S')),'w')
file.write('\n')
file.write('\n')
file.write(fivedayago.strftime('%Y-%m-%d %H:%M:%S'))
file.write('\n')
file.write('\n')
file.close()

