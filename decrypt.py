import convert_num
import convert_text
import universal_functions as uni


def de_message(blocks, d, n, max_len, last_len):
    de_b = ""
    for i in range(len(blocks)):
        form = f'0{len(blocks[i])}b'
        num = int(blocks[i], 2)
        e_num = uni.power(num, d, n)
        de_block = format(e_num, form)
        if max_len > n.bit_length() and de_block[0] == '0':
            de_block = de_block[1:]
        if i == len(blocks) - 1:
            de_block = de_block[-last_len:]
        de_b += de_block

    de_n = int(de_b, 2)
    return de_n


def decrypt(num, d, n, m_l, last_l, all_len):
    blocks = convert_num.split_message(n, int(num), m_l + 1, all_len)
    d_m = de_message(blocks, d, n, m_l + 1, last_l)

    text = convert_text.convert_number_to_text(str(d_m))
    return text
