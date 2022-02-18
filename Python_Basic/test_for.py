#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-

list1 = ['aaa', 111, (4, 5), 2.01]
list2 = ['bbb', 333, 111, 3.14, (4, 5)]

# 方法一
# for x in list1:
#     #x循环list2
#     if x in list2:
#         print(x,'in list1 and list2')
#     else:
#         print(x ,'only in list1')

# 方法二
def comp(a,b):
    for x in a:
       if x in b:
            print(x, ' in list1 and list2')
       else:
            print(x, ' only in list1')

comp(list1,list2)
