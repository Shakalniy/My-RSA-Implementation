def split_message(n, m, max_len, all_l):
    form = f'0{all_l}b'
    n_b = bin(n)[2:]
    m_b = format(m, form)
    l_n = max(len(n_b), max_len)
    l_m = len(m_b)
    blocks = []

    if l_m < l_n:
        return [m_b]

    for i in range(0, l_m, l_n - 1):
        if l_m - i >= l_n - 1:
            m_i = m_b[i: i + l_n - 1]
            blocks.append(m_i)
        else:
            m_i = m_b[i: l_m]
            blocks.append(m_i)

    return blocks

