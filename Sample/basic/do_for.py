#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#   字符串连接方式:
# 1.直接用 “+” 来连接两个字符串
# 2.两个字符串用“逗号”隔开(字符串之间会多出一个空格)
# 3.符号“%”连接一个字符串和一组变量,自动用右边变量组中的变量替换

L = ['bart','Lisa','Adam']
for name in L:
    print('hello,'+name+'!')
for name in L:
    print('hello,%s!'%name)
for name in L:
    print('hello,',name,'!')
