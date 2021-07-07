#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-

l1 = [4,5,7,1,3,9,0]
#引用，拷贝
l2 = list(l1)
#对l2进行排序
l2.sort()

#for循环打印
for i in range (len(l1)):
	print(l1[i],l2[i])