import math
""" In this app we're gonna try to find the M.C.M
    ( Maximum Common Multiple ) of a bunch of numbers
"""


def gcd(x, y, d):
    if x < y:
        z = x
    if d < y:
        z = d
    else:
        z = y

    while True:
        if (z % x == 0) and (z % y == 0) and (z % d == 0):
            gcd = z
            break
        z -= 1
    return gcd


print("Greatest Common Divisor (Handwritten):", gcd(8, 4, 2))

# or we just can use this methods for saved work

print("Greatest Common Divisor (Math Method):", math.gcd(8, 4, 2))

