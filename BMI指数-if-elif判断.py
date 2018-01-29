#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#注意：
# float() 函数用于将整数和字符串转换成浮点数
# input()返回的是字符串
# 必须通过float()将字符串转换为浮点数
# 才能用于数值计算:

s=input('please enter your height (m.):')
z=input('please enter your weight (kg.):')
height=float(s)
weight=float(z)
bmi=weight/(height**2)
if bmi<18.5:
    print('bmi指数:%.2f;你的体重过轻，多吃点'%bmi)
elif 25>=bmi>18.5:
    print('bmi指数:%.2f;你的体重正常'%bmi)
elif 28>=bmi>25:
    print('bmi指数:%.2f;你的体重过重，注意啦'%bmi)
elif 32>=bmi>28:
    print('bmi指数:%.2f;你的体重肥胖，控制'%bmi)
else:
    print('bmi指数:%.2f;严重肥胖，节制'%bmi)
