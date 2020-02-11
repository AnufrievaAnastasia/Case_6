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
order = 6
size = 10000
ice(order, size)