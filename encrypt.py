import convert_text
import universal_functions as uni


def encrypt(text, e, n):
    m = int(convert_text.convert_text_to_number(text))
    form = f'0{m.bit_length()}b'
    n_b = bin(n)[2:]
    m_b = format(m, form)
    l_n = len(n_b)
    l_m = len(m_b)
    en_b = ""
    max_len = 0
    last_len = 0
    for i in range(0, l_m, l_n - 1):
        if l_m - i >= l_n - 1:
            m_i = m_b[i: i + l_n - 1]
        else:
            m_i = m_b[i: l_m]
            last_len = len(m_i)
        num = int(m_i, 2)
        e_num = uni.power(num, e, n)
        if e_num.bit_length() > max_len:
            max_len = e_num.bit_length()
        form = f'0{max_len}b'
        en_b += format(e_num, form)
    en_n = int(en_b, 2)
    return en_n, max_len, last_len, len(en_b)
