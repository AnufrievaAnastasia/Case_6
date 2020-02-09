from turtle import *

def tree(size):
    if size < 4:
        return
    else:
        forward(size)
        left(35)
        tree(size/2)
        right(70)
        tree(size/2)
        left(35)
        back(size)
    return


left(90)
tree(100)


