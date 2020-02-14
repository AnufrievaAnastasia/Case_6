from turtle import *


def levi(order, size):
    if order == 0:
        forward(size)
    else:
        left(45 * order)
        levi(order - 1, size / 2)
        right(90)
        levi(order - 1, size / 2)


order = int(input())
size = int(input())

levi(order, size)