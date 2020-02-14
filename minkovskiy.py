from turtle import *


def mink(order, size):
    if order == 0:
        forward(size)
    else:
        mink(order - 1, size / 4)
        left(90)
        mink(order - 1, size / 4)
        right(90)
        mink(order - 1, size / 4)
        right(90)
        mink(order - 1, size / 2)
        left(90)
        mink(order - 1, size / 4)
        left(90)
        mink(order - 1, size / 4)
        right(90)
        mink(order - 1, size / 4)

order = int(input())
size = int(input())

mink(order, size)