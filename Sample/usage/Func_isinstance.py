#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  isinstance()
#  语法： isinstance(abject,classinfo)
#  参数： 
#         object: 实例对象
#         classinfo: 可以是直接或间接类名、基本类型或者有它们组成的元组
#         返回值: 如果对象的类型与参数二的类型（classinfo）相同则返回True。否则返回 False

a=5
print(isinstance(a,int))  # 判断a是否是整数类型
# True
print(isinstance(a,str))  # 判断a是否是字符串类型
# False
print(isinstance(a,(int,int,list)))  # 是元组中的一种则返回 True
# True
