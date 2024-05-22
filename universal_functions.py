import sys


sys.setrecursionlimit(3000)


def power(x, y, n):
    if y == 0:
        return 1
    temp = power(x, int(y // 2), n)
    if y % 2 == 0:
        return (temp * temp) % n
    else:
        return (x * temp * temp) % n


def gcd(a, b):
    while a != 0 and b != 0:
        if a >= b:
            a %= b
        else:
            b %= a
    return a or b
