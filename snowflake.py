from turtle import *

def ice(order, size):
    if order == 0:
        forward(size)
    else:
        ice(order-1, size/2)
        left(90)
        ice(order - 1, size / 4)
        right(180)
        ice(order - 1, size / 4)
        left(90)
        ice(order - 1, size / 2)

def snowflake(order, size):
        ice(order, size)
        right(90)
        ice(order, size)
        right(90)
        ice(order, size)
        right(90)
        ice(order, size)
        right(180)
        ice(order, size)
        left(90)
        ice(order, size)
        left(90)
        ice(order, size)
        left(90)
        ice(order, size)



order = int(input())
size = int(input())

snowflake(order, size)