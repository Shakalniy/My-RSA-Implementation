import gen_keys
import gen_prime_nums as prime
import universal_functions as uni
import encrypt
import decrypt
import time


size = 1024


def print_large_num(n):
    s = str(n)
    for i in range(0, len(s), 100):
        if i + 100 < len(s):
            print(s[i: i + 100])
        else:
            print(s[i: i + (len(s) % 100)])
    return ""


def rsa():
    # конвертация текста
    text = input("Введите сообщение: ")
    t = time.time()
    print("Исходное сообщение:", text)

    # генерация p и q
    is_correct = False
    p, q, n = 0, 0, 0
    while not is_correct:
        p = prime.gen_secure_prime_num(size)
        q = prime.gen_secure_prime_num(size)
        n = p * q
        if max(p, q) - min(p, q) > 2**(size/4):
            is_correct = True

    print("Сгенерированные параметры:")
    print(f"p = {print_large_num(p)}")
    print(f"q = {print_large_num(q)}")
    print(f"n = {print_large_num(n)}")

    # генерация ключей
    phi_n = (p - 1) * (q - 1)
    nod = uni.gcd(p-1, q-1)
    nok = phi_n // nod
    e, d = gen_keys.gen_keys(n, phi_n, nok)

    print("Сгенерированное ключи:")
    print(f"e = {print_large_num(e)}")
    print(f"d = {print_large_num(d)}")

    # шифрование
    e_m, m_l, last_l, all_len = encrypt.encrypt(text, e, n)
    print("Зашифрованное сообщение:")
    print_large_num(e_m)
    # дешифрование
    de_text = decrypt.decrypt(e_m, d, n, m_l, last_l, all_len)
    print("Расшифрованное сообщение:", de_text)

    print("Время работы программы:", (time.time() - t).__round__(2))
