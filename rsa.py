import gen_keys
import gen_prime_nums as prime
import universal_functions as uni
import encrypt
import decrypt
import convert_file
import time


size = 1024


def print_large_num(pred, n):
    s = str(n)
    l = len(s)
    print(pred, end="")
    for i in range(0, l, 100):
        if i + 100 < len(s):
            print(s[i: i + 100])
        else:
            print(s[i: l])
    return ""


def rsa():
    # конвертация текста
    file_name = input("Введите имя файла: ")
    t = time.time()

    # генерация p и q
    is_correct = False
    p, q, n = 0, 0, 0
    while not is_correct:
        p = prime.gen_secure_prime_num(size)
        q = prime.gen_secure_prime_num(size)
        if max(p, q) - min(p, q) > 2**(size/4):
            is_correct = True

    n = p * q
    print("Сгенерированные параметры:")
    print_large_num("p = ", p)
    print_large_num("q = ", q)
    print_large_num("n = ", n)

    # генерация ключей
    phi_n = (p - 1) * (q - 1)
    nod = uni.gcd(p-1, q-1)
    nok = phi_n // nod
    e, d = gen_keys.gen_keys(n, phi_n, nok)

    print("Сгенерированное ключи:")
    print_large_num("e = ", e)
    print_large_num("d = ", d)

    bytes = convert_file.convert_file_to_bits(file_name, n)
    # шифрование
    e_m, last_l = encrypt.encrypt(bytes, e, n)
    # print("Зашифрованное сообщение:")
    # print_large_num(e_m)
    bytes = convert_file.convert_to_bytes(e_m)
    convert_file.write_file(bytes, file_name, "en")
    # дешифрование
    de_bits = decrypt.decrypt(e_m, d, p, q, n, last_l)
    # print("Расшифрованное сообщение:", de_bits)
    bytes = convert_file.convert_to_bytes(de_bits)
    convert_file.write_file(bytes, file_name, "de")

    print("Время работы программы:", (time.time() - t).__round__(2))
