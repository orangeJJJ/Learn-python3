#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
def quadratic(a,b,c):
    if not isinstance(a, (int, float)):
        raise TypeError('bad operand type')
    if not isinstance(b, (int, float)):
        raise TypeError('bad operand type')
    if not isinstance(c, (int, float)):
        raise TypeError('bad operand type')
    if b*b-4*a*c<0:
        return '无解'
    else:
        x1=(-b+math.sqrt(b*b-4*a*c))/2*a    #计算平方根可以调用math.sqrt()函数：
        x2=(-b-math.sqrt(b*b-4*a*c))/2*a
        return x1,x2
a=float(input('请输入一元二次方程中的a:'))
b=float(input('请输入一元二次方程中的b:'))
c=float(input('请输入一元二次方程中的c:'))
print(quadratic(a,b,c))

