#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-

#现在有个字符串word = " scallywag"，创建一个变量sub_word，通过切片的方式获得字符串"ally"，将字符串的内容赋予sub_word。

word = " scallywag" #给word赋值
news = word.strip() #剔除空格
word1= news.replace('sc','')    #切掉“sc”
sub_word = word1.replace('wag','')  #切掉“wag”

print (sub_word)