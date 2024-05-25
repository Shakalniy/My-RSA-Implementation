import sys


def power(x, y, n):
    res, v, c = 1, x, y
    if c & 1:
        res = v
    c >>= 1
    while c > 0:
        v = v * v % n
        if c & 1:
            res = v * res % n
        c = c >> 1
    return res


def gcd(a, b):
    while a != 0 and b != 0:
        if a >= b:
            a %= b
        else:
            b %= a
    return a or b
