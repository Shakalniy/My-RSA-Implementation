import gen_prime_nums as prime
import universal_functions as uni
import math
import random


err_mes = "Проверка не пройдена.\n"
suc_mes = "Проверка пройдена.\n"


def check_one_prime(p):
    if prime.low_level_check(p):
        if prime.check_prime(p):
            return True
    return False


def check_primes_is_correct(p, q):
    is_prime_p = check_one_prime(p)
    is_prime_q = check_one_prime(q)

    if is_prime_p and is_prime_q:
        print("p и q - простые числа.")
        return True

    if not is_prime_p and not is_prime_q:
        print("Числа p и q не являются простыми.")
    elif not is_prime_p and is_prime_q:
        print("Число p не является простым. Число q является простым.")
    else:
        print("Число p является простым. Число q не является простым.")

    return False


def check_exp_is_correct(e, d, phi_n):
    nod = uni.gcd(e, phi_n)
    r = (e * d) % phi_n
    if e <= 1 or e >= phi_n:
        print(f"Открытая экспонента e должна быть такой, что: 1 < e < φ(n).")
    elif nod != 1:
        print(f"Открытая экспонента e не взаимно проста с φ(n). НОД({e}, {phi_n}) = {nod}.")
    elif r != 1:
        print("Секретная экспонента не является обратной к открытой экспоненте e по модулю φ(n).")
        print(f"{e} * {d} mod({phi_n}) = {r}.")
    else:
        print("e и d - корректные экспоненты для RSA")
        return True

    return False


def fermat_attack(n):
    A = math.isqrt(n) + 1
    B = A**2 - n
    p, q = 0, 0
    b = math.isqrt(B) + 1
    i = 0
    while p * q != n and i < 100000:
        if b**2 != B:
            A = math.isqrt(b**2 + n)
        p = A + b
        q = A - b
        b += 1
        i += 1

    if p * q == n:
        return True
    else:
        return False


def check_fermat_attack(p, q, n):
    diff = abs(p - q)
    n_len = n.bit_length()
    low_lim = (2 ** math.ceil(n_len / 4))
    if diff > low_lim:
        if not fermat_attack(n):
            print(f"Данная криптосистема устойчива к атаке Ферма:\np - q = {diff} > {low_lim}.")
        else:
            print(f"Данная криптосистема не устойчива к атаке Ферма, из-за слишком маленьких p и q.")
    else:
        print(f"Данная криптосистема не устойчива к атаке Ферма:\np - q = {diff} <= {low_lim}.")


def equation(a, b, c):
    discr = b ** 2 - 4 * a * c

    if discr > 0:
        x1 = (-b + math.isqrt(discr)) // (2 * a)
        x2 = (-b - math.isqrt(discr)) // (2 * a)
        return [int(x1), int(x2)]
    else:
        return False


def viner_attack(e, n):
    a, q = divmod(e, n)  # целая и дробная части
    t = n
    res = [a]
    while q != 0:
        next_t = q
        a, q = divmod(t, q)
        t = next_t
        res.append(a)

    fractions = [[0, 1], [1, res[1]]]
    for i in range(2, len(res)):
        numerator = fractions[i - 2][0] + fractions[i - 1][0] * res[i]
        denominator = fractions[i - 2][1] + fractions[i - 1][1] * res[i]
        fractions.append([numerator, denominator])

    for i in range(1, len(fractions)):
        k, d = fractions[i][0], fractions[i][1]
        phi_n = (e * d - 1) // k
        b = -(n - phi_n + 1)
        roots = equation(1, b, n)
        if roots:
            pr = roots[0] * roots[1]
            if pr == n:
                return True

    return False


def check_viner_attack(e, d, n):
    low_lim_e = math.isqrt(n) + 1
    low_lim_d = (math.isqrt(math.isqrt(n) + 1) + 1) // 3
    reasons = ""

    if e <= low_lim_e and d <= low_lim_d:
        print(f"Данная криптосистема не устойчива к атаке Винера:\ne = {e} <= {low_lim_e}\nd = {d} <= {low_lim_d}.")
    else:
        if viner_attack(e, n):
            print(f"Данная криптосистема не устойчива к атаке Винера, из-за слишком маленьких p и q.")
        else:
            if e > low_lim_e:
                reasons += f"\ne = {e} > {low_lim_e}"
            if d > low_lim_d:
                reasons += f"\nd = {d} > {low_lim_d}"
            print(f"Данная криптосистема устойчива к атаке Винера:{reasons}.")


def re_encryption_attack(e, n, c):
    i = 0
    x = c
    while (x != c or i == 0) and i < 100000:
        x = uni.power(x, e, n)
        i += 1

    if x != c:
        return False
    else:
        return True


def check_big_prime_divs(p, letter, letter1):
    if p.bit_length() < 256:
        print(f"Число {letter} не является большим простым числом.")
        return False
    phi_p = p - 1
    k = 2
    while phi_p % k != 0 or k < math.isqrt(phi_p):
        if phi_p % k == 0:
            r = phi_p // k
            if prime.check_prime(r):
                break
        k += 1

    r = phi_p // k

    if not prime.check_prime(r):
        print(f"Число {letter} не имеет большого простого делителя")
        return False
    else:
        print(f"Число {letter} имеет большой простой делитель.")
        print(f"{letter} - 1 = k * {letter1} = {k} * {r}.")
        phi_r = r - 1
        k1 = 2
        while phi_r % k1 != 0 or k1 < math.isqrt(phi_r):
            if phi_r % k1 == 0:
                r1 = phi_r // k1
                if prime.check_prime(r1):
                    break
            k1 += 1

        r1 = phi_r // k1

        if not prime.check_prime(r1):
            print(f"Число {letter1} не имеет большого простого делителя.")
        else:
            print(f"Число {letter1} имеет большой простой делитель.")
            print(f"{letter1} - 1 = k1 * {letter1}1 = {k1} * {r1}.")

    return True


def check_re_encryption_attack(e, n):
    m = random.randint(2, n - 1)
    c = uni.power(m, e, n)
    if re_encryption_attack(e, n, c):
        print(f"Данная криптосистема не устойчива к атаке повторным шифрованием.")
    else:
        print(f"Данная криптосистема устойчива к атаке повторным шифрованием.")


def check_defend_to_attacks(p, q, e, d, n, phi_n):
    print("Проверка устойчивости данной крипосистемы:")
    n = p * q
    phi_n = (p - 1) * (q - 1)
    if n.bit_length() < 1024:
        print(f"Размер ключей {n.bit_length()} бит не является надёжным, рекомендуется использовать размер ключей не менее 1024 бит.")

    check_fermat_attack(p, q, n)
    check_viner_attack(e, d, n)
    if not (check_big_prime_divs(p, "p", "r") or check_big_prime_divs(q, "q", "s")):
        check_re_encryption_attack(e, n)
    else:
        print(f"Данная криптосистема устойчива к атаке повторным шифрованием.")


def check_key():
    print("Введите параметры вашей криптосистемы:")
    p = int(input("p = "))
    q = int(input("q = "))
    e = int(input("e = "))
    d = int(input("d = "))
    print("Проверка на корректность введённых данных:")
    if check_primes_is_correct(p, q):
        n = p * q
        phi_n = (p - 1) * (q - 1)
        if check_exp_is_correct(e, d, phi_n):
            print(suc_mes)
            check_defend_to_attacks(p, q, e, d, n, phi_n)
        else:
            print(err_mes)
    else:
        print(err_mes)
