#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-

#创造自己的语言 我们将在英语的基础上创建自己的语言：在单词的最后加上-，
#然后将单词的第一个字母拿出来放到单词的最后，然后在单词的最后加上y，例如，Python，就变成了ython-Py

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


