from turtle import *


def koch2(order, size):
    if order == 0:
        forward(size)
    else:
        koch2(order-1, size/3)
        left(60)
        koch2(order - 1, size / 3)
        right(120)
        koch2(order - 1, size / 3)
        left(60)
        koch2(order - 1, size / 3)
order = 2
size = 100
koch2(order, size)
right(120)
koch2(order, size)
right(120)
koch2(order, size)
