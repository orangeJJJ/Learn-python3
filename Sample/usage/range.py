#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# range()
# 语法： range(start,stop[,step])
# 参数：
#        start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）。
#          end: 计数到 end 结束，但不包括 end。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5。
#         step: 步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)。

print(range(1, 5))
# range(1, 5)

print(tuple(range(1, 5)))
# (1, 2, 3, 4)

print(list(range(1, 5)))
# [1, 2, 3, 4]


for i in range(1, 5):
    print(i)
# 1
# 2
# 3
# 4

print(list(range(10)))    # 从 0 开始到 10
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(range(1, 11)))    # 从 1 开始到 11
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(range(0, 30, 5)))    # 步长为 5
# [0, 5, 10, 15, 20, 25]

print(list(range(0, 10, 3)))    # 步长为 3
# [0, 3, 6, 9]

print(list(range(0, -10, -1)))    # 负数
# [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]

print(list(range(0)))
# []

print(list(range(1, 0)))
# []










