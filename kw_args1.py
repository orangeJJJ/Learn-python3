#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def person(name,age,**kw):    # **kw 关键字参数，关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
    print(name,age,kw)

person('mary', 7, city = 'IV')
# mary 7 ('city' : 'IV')
person('pryg', 74)
# pryg 74 ()



def person(name, age, *, city, job):    # 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
    print(name, age, city, job)

person('Tom', 7,city = 'USK',job = 'tebu')    # 命名关键字参数必须传入参数名，这和位置参数不同。
# Tom 7 USK tubu

# person('Bob', 82)    错误



# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person(name, age, *args, city, job):    # *args 可变参数，可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
    print(name, age, args, city, job)

person('Ric', 15, '来啊', city = 'Beijing', job = 'pH')
# Ric 15 ('来啊',) Beijing pH

person('Yfg', 54, 'x', city='uuugd', job='yyi')
# Yfg 54 ('x',) uuugd yyi

person('Joj', 2, 33, city='hjz', job='spH')
# Joj 2 ('33',) hjk spH

person('Joj', 2, city='hjz', job='spH')
# Joj 2 () hjk spH









