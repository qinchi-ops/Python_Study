#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-

#方法1
# a = 'Python'
# b = list(a) #将string转换成List
# news = b[1]+b[2]+b[3]+b[4]+b[5]+'-'+b[0]+'y' #拼接
# print (news)

#方法2
a = 'Python'
b = list(a) #将string转换成List
b.append('-') #在末尾增加"-"
news = b[1:]+b[:1]  #在末尾增加"P"
news.append('y') #在末尾增加"y"
letter=''.join(news)
print(letter)


