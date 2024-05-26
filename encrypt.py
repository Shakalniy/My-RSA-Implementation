import convert_file
import universal_functions as uni


def encrypt(bits, e, n):
    max_len = n.bit_length() - 1
    en_bits = ""
    last_l = 0
    for i in range(0, len(bits), max_len):
        m = 0
        if i + max_len <= len(bits):
            m = bits[i: i + max_len]
        else:
            m = bits[i: len(bits)]
            last_l = len(m)
        m = int(m, 2)
        c = uni.power(m, e, n)
        en_bits += format(c, f'0{max_len + 1}b')

    return en_bits, last_l
