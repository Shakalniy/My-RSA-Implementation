import universal_functions as uni
import gen_keys


def crt(c, d, p, q, n):
    d_p = d % (p - 1)
    d_q = d % (q - 1)

    m_p = uni.power(c, d_p, p)
    m_q = uni.power(c, d_q, q)

    m_p_obr = gen_keys.gcd_extended(p, q)[2]
    m_q_obr = gen_keys.gcd_extended(q, p)[2]

    m = (m_p * q * m_p_obr + m_q * p * m_q_obr) % n

    return m


def decrypt(bits, d, p, q, n, last_l):
    max_len = n.bit_length()
    de_bits = ""
    for i in range(0, len(bits), max_len):
        c = bits[i: i + max_len]

        c = int(c, 2)
        m = crt(c, d, p, q, n)
        if i + max_len == len(bits):
            de_bits += format(m, f'0{last_l}b')
        else:
            de_bits += format(m, f'0{max_len - 1}b')

    return de_bits
