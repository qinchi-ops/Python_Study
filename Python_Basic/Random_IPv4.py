#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-
# -*- coding: UTF-8 -*-

import random   #导入random模块

#随机产生IP地址四个分段的数字

section1 = random.randint(1, 255)
section2 = random.randint(1, 255)
section3 = random.randint(1, 255)
section4 = random.randint(1, 255)

#random_ip = str(section1) + '.' +  str(section2)
random_ip = str(section1) + '.' + str(section2) + '.' +  str(section3) + '.' + str(section4)
#如果不转换数字到字符串会变成这些数值相加
print(random_ip)
#打印随机IP
