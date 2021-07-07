#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-
import re

port_list = ['eth 1/101/1/42','eth 1/101/1/26','eth 1/101/1/23','eth 1/101/1/7','eth 1/101/2/46','eth 1/101/1/34','eth 1/101/1/18','eth 1/101/1/13','eth 1/101/1/32','eth 1/101/1/25','eth 1/101/1/45','eth 1/101/2/8']
# l1 = 'eth 1/101/1/42'
# # a = l1.split('/')
# c = re.search('^eth (\d)\/(\d\d\d)\/(\d)\/(\d\d)',l1).groups()
# d = re.search('^eth (\d)\/(\d\d\d)\/(\d)\/(\d\d)',l1).groups()[2]
result = sorted(port_list, key=lambda x: x in re.search('^eth (\d)\/(\d\d\d)\/(\d)\/(\d\d)',port_list).groups())


#抄Google的方法，自己只想到了 x.split('/')
#result = sorted(port_list, key=lambda name: [int(part) if part.isdigit() else part for part in name.split('/')])
#port_list.sort(key=lambda x: x.split('/')[-1])

#方法一split
#方法二regular expression re.match "^eth "
#result = sorted(port_list, key=lambda x: (x.split('/')[3],x.split('/')[2]))
#result = sorted(port_list, key=lambda x: x.split('/')[3])

print(result)
