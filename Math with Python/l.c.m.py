"""" In this app we're gonna try to find the l.c.m
    (Lowest common multiple) of a bunch of numbers
"""


def lcm(x, y, d):
    if x > y:
        z = x
    if d > y:
        z = d
    else:
        z = y

    while True:
        if (z % x == 0) and (z % y == 0) and (z % d == 0):
            lcm = z
            break
        z += 1
    return lcm


print("Lowest Common Multiple (Handwritten):", lcm(5, 15, 30))

# or we just can use this methods for saved work
import math

print("Lowest Common Multiple (Math Method):", math.lcm(5, 15, 30))
