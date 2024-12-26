#scope resolution
# LEGB = LOCAL ENCLOSED GLOBAL BUILT IN

# x = 2
from math import e
# def func1():
#     x = 1
#     print(x)
# def func2():
#     print(x)

# func1()
# func2()

e = 3
def fun1():
    print(e)

fun1()