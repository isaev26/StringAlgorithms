def naive_z_values(s):
    n = len(s)
    zp = [0]*n
    for i in range(1, n):
        j = i
        while j < n and s[j] == s[j - i]:
            j = j + 1
        zp.append(j - i)
    print("Массив Z-значений", zp)


def str_comp(s, n, i1, i2):
    eq_len = 0
    try:
        while i1 < n and i2 < n and s[i1] == s[i2]:
            eq_len += 1
            i1 += 1
            i2 += 1
    except IndexError:
        return eq_len
    else:
        return eq_len


def prefix_z_values(s):
    n = len(s)
    l, r = 0, 0
    zp = [0] * n
    for i in range(1, n):
        # zp.append(0)
        if i >= r:
            zp[i] = str_comp(s, n, 0, i)
            l = i
            r = l + zp[i]
        else:
            j = i - l
            if zp[j] < r - i:
                # так как мы находимся в подстроке, совпадающей с префиксом всей строки
                zp[i] = zp[j]
            else:
                zp[i] = r - i + str_comp(s, n, r - i, r)
                l = i
                r = l + zp[i]
    print("Алгоритм вычисления массива Z-значений", zp)
    return zp


def str_comp_back(s, i1, i2):
    eqLen = 0
    try:
        while i1 >= 0 and i2 >= 0 and s[i1-1] == s[i2-1]:
            eqLen += 1
            i1 -= 1
            i2 -= 1
    except IndexError:
        return eqLen
    else:
        return eqLen


def suffix_z_values(s):
    n = len(s)
    l = r = n - 1
    zs = [0]*n
    for i in range(n - 2, 0, -1):
        if i <= l:
            zs[i] = str_comp_back(s, i, n - 1)
            r = i
            l = r - zs[i]
        else:
            j = n - (r + 1 - i)
            if zs[j] < i - l:
                zs[i] = zs[j]
            else:
                zs[i] = i - l + str_comp_back(s, l, n - i + l)
                r = i
                l = r - zs[i]
    print("Вычисление массива Z-значений суффиксов", zs)


def zp_to_bpm(zp, n):
    bpm = [0 for i in range(n)]
    for j in range(n - 1, 0, -1):
        i = j + zp[j] - 1
        bpm[i] = zp[j]
    print("Алгоритм: zp в bpm", bpm)


def zp_to_bp(zp, n):
    bp = [0] * n
    for j in range(1, n):
        tmp = j + zp[j] - 1
        for i in range(tmp, j-1, -1):
            if bp[i]:
                break
            bp[i] = i - j + 1
    print("Алгоритм zp в bp", bp)
    return bp


def ValGrow(n_arr, n, n_pos, n_val):
    n_seq_len = 0
    try:
        while n_pos < n and n_arr[n_pos] == n_val:
            n_seq_len += 1
            n_pos += 1
            n_val += 1
    except IndexError:
        return n_seq_len
    else:
        return n_seq_len


def bp_to_zp(bp, n):
    l, r = 0, 0
    zp = [0] * n
    for i in range(1, n):
        if i >= r:
            zp[i] = ValGrow(bp, n, i, 1)
            l = i
            r = l + zp[i]
        else:
            j = i - l
            if zp[j] < r - i:
                zp[i] = zp[j]
            else:
                zp[i] = r - i + ValGrow(bp, n, r, r - i - 1)
                l = i
                r = l + zp[i]
    print("Алгоритм BP в ZP", zp)


if __name__ == '__main__':
    with open("text.txt", "r") as file:
        S = file.readline()
        print("Строка-> " + S)
        n = len(S)

    naive_z_values(S)
    zp = prefix_z_values(S)
    suffix_z_values(S)
    zp_to_bpm(zp, n)
    bp = zp_to_bp(zp, n)
    bp_to_zp(bp, n)
