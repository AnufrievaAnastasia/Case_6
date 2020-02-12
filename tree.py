from turtle import *

def tree(size, corner ):
    if size < 4:
        return
    else:
        forward(corner * 10)
        left(35)
        tree(size / 2, corner * 0.8)
        right(70)
        tree(size / 2, corner * 0.8)
        left(35)
        back(corner * 10)
    return


corner = int(input())
size = int(input())

left(90)
tree(size, corner)

