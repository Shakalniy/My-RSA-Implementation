import math
import gen_prime_nums as prime


def gcd_extended(num1, num2):
    if num1 == 0:
        return num2, 0, 1
    else:
        div, x, y = gcd_extended(num2 % num1, num1)
    return div, y - (num2 // num1) * x, x


def gen_open_exp(n, phi_n, nok):
    e = prime.gen_prime_num(phi_n.bit_length() - 1)
    while e < math.isqrt(n):
        e += nok

    return e


def gen_secret_exp(e, phi_n, n, nok):
    min_d = math.isqrt(math.isqrt(n)) // 3
    d = gcd_extended(phi_n, e)[2]
    while d < min_d:
        d += nok

    return d


def gen_keys(n, phi_n, nok):
    e = gen_open_exp(n, phi_n, nok)
    d = gen_secret_exp(e, phi_n, n, nok)
    return e, d

