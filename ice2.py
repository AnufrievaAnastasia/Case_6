from turtle import *


def ice2(order, size):
    if order == 0:
        forward(size)
    else:
        ice2(order - 1, size / 2)
        left(135)
        ice2(order - 1, size / 4)
        right(180)
        ice2(order - 1, size / 4)
        left(90)
        ice2(order - 1, size / 4)
        right(180)
        ice2(order - 1, size / 4)
        left(135)
        ice2(order - 1, size / 2)

order = int(input())
size = int(input())

ice2(order, size)
