# Anufrieva A. 67%
# Zhuravleva A. 50%

from turtle import *


def ice(order, size):
    if order == 0:
        forward(size)
    else:
        ice(order-1, size / 2)
        left(90)
        ice(order - 1, size / 4)
        right(180)
        ice(order - 1, size / 4)
        left(90)
        ice(order - 1, size / 2)

order = int(input())
size = int(input())

ice(order, size)