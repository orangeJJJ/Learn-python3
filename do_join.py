#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  join()
#  功能：连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串
#  语法：'sep'.join(seq) 以sep作为分隔符，将seq所有的元素合并成一个新的字符串
#  参数：
#        sep：分隔符。可以为空
#        seq：要连接的元素序列、字符串、元组、字典
#        返回值：返回一个以分隔符sep连接各个元素后生成的字符串

#对序列进行操作（分别使用' '与':'作为分隔符）

seq1 = ['hello','good','boy','douudo']
print(' '.join(seq1))
print(':'.join(seq1))

#对字符串进行操作

seq2 = 'hello good boy douudo'
print(':'.join(seq2))

#对元组进行操作

seq3 = ('hello','good','boy','douudo')
print(':'.join(seq3))

#对字典进行操作

seq4 = {'hello':1,'good':2,'boy':3,'douudo':4}
print(':'.join(seq4))



