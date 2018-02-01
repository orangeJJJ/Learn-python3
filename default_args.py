#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def add_end (L=[]) :
    L.append ('END')
    print (L)

add_end ([1,2,3])
# [1, 2, 3, 'END']

add_end (['x','y','z'])
# ['x', 'y', 'z', 'END']

add_end ()
# ['END']

add_end ()
# ['END', 'END']

add_end ([3,4,5])
# [3, 4, 5, 'END']

add_end ()
# ['END', 'END', 'END']    #默认参数必须指向不变对象！

def add_end (L=None):
    if L is None:
        L = []
    L.append ('END')
    print (L)
    
add_end ()
# ['END']

add_end ()
# ['END']    #不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。


