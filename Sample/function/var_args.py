#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def hello(greeting, *args):    # 剩余的参数以元组的形式存储在 args（args 名称你可以自行定义）
    if (len(args)==0):
        print('%s!' % greeting)
    else:
        print('%s,%s!'% (greeting,','.join(args)))

hello('Hi') # => greeting='Hi', args=()
# Hi!

hello('Hi', 'Sarah') # => greeting='Hi', args=('Sarah')
# Hi,Sarah!

hello('Hello', 'Michael', 'Bob', 'Adam') # => greeting='Hello', args=('Michael', 'Bob', 'Adam')
# Hello,Michael,Bob,Adam!

names = ('Bart', 'Lisa')
hello('Hello', *names) # => greeting='Hello', args=('Bart', 'Lisa')
# Hello,Bart,Lisa!

