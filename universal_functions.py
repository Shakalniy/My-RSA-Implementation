def power(x, y, n):
    c = 1
    while y > 0:
        if y % 2 == 0:
            x = (x * x) % n
            y = y >> 1
        else:
            c = (c * x) % n
            y -= 1
    return c


def gcd(a, b):
    while a != 0 and b != 0:
        if a >= b:
            a %= b
        else:
            b %= a
    return a or b
