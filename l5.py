def position_list(s):
    m = len(s)
    offset_table = {}
    for i in range(256):
        offset_table[chr(i)] = m
    for i in range(m - 1, -1, -1):
        if offset_table[s[i]] == m:
            offset_table[s[i]] = [i]
        else:
            offset_table[s[i]].append(i)
    return offset_table


def bad_char_shift(pl, char_bad, pos_bad):
    if pos_bad < 0:
        return 1
    n_pos = -1  # искомая позиция слева от плохого символа char_bad
    List = pl[char_bad]
    try:
        for i in range(len(List)):
            if List[i] < pos_bad:
                n_pos = List[i]
                break
    except TypeError:
        return pos_bad - n_pos
    else:
        return pos_bad - n_pos


def Suffix_Border_Array(s):
    n = len(s)
    bs = [0 for i in range(n)]
    for i in range(n - 2, -1, -1):
        bs_left = bs[i + 1]
        while bs_left and s[i] != s[n - bs_left - 1]:
            bs_left = bs[n - bs_left]
        if s[i] == s[n - bs_left - 1]:
            bs[i] = bs_left + 1
        else:
            bs[i] = 0
    return bs


def BS_to_BSM(bs, n):
    bsm = [0]*n
    bsm[0] = bs[0]
    for i in range(n-2, 0, -1):
        if(bs[i]and (bs[i]+1 == bs[i-1])):
            bsm[i] = bsm[n-bs[i]]
        else:
            bsm[i] = bs[i]
    return bsm
# ###########################################


def bs_to_ns(bs, m):
    ns = [-1] * m
    for j in range(m):
        if bs[j]:
            k = m - bs[j] - 1
            ns[k] = j
    return ns


def bs_to_br(bs, m):
    br = [0]*m
    curr_border = bs[0]
    k = 0
    while curr_border:
        for k in range(m - curr_border):
            br[k] = curr_border
        curr_border = bs[k + 1]
    return br


def good_suffix_shift(nsx, br, pos_bad, m):
    if pos_bad == m - 1:
        return 1
    if pos_bad < 0:
        return m - br[0]
    copy_pos = nsx[pos_bad]
    if copy_pos >= 0:
        shift = pos_bad - copy_pos + 1
    else:
        shift = m - br[pos_bad]
    return shift


def BM(p, t, h):
    pl = position_list(p)
    m, n = len(p), len(t)
    bs = Suffix_Border_Array(p)
    br = bs_to_br(bs, m)
    if h:
        bs = BS_to_BSM(bs, m)
    nsx = bs_to_ns(bs, m)
    print(nsx)
    n_text_r = m
    while n_text_r <= n:
        k = m - 1
        i = n_text_r - 1
        while k >= 0 and p[k] == t[i]:
            k -= 1
            i -= 1
        if k < 0:
            print("Вхождение с позиции", i + 1)
        n_shift = max(bad_char_shift(
            pl, t[i], k), good_suffix_shift(nsx, br, k, m))
        n_text_r += n_shift


def gorner_2_mod(s, m, q):
    res = 0
    for i in range(m):
        res = (res << 1 + ord(s[i])) % q
    return res


def KR(p, t, q):
    m, n = len(p), len(t)
    p2m = 1
    for i in range(m - 1):
        p2m = (p2m << 1) % q
    hp = gorner_2_mod(p, m, q)
    ht = gorner_2_mod(t, m, q)
    for j in range(n - m + 1):
        if ht == hp:
            k = 0
            while k < m and p[k] == t[j+k]:
                k += 1
            if k == m:
                print("Вхождение с позиции", j)
        try:
            ht = ((ht - p2m * ord(t[j])) << 1 + ord(t[j+m])) % q
        except IndexError:
            pass
        if ht < 0:
            ht += q


if __name__ == '__main__':
    with open("text.txt", "r") as file:
        S = file.readline()
        print("String-> " + S)
        n = len(S)

    p = input("Введите подстроку: ")
    print("Алгоритм Бойера-Мура")
    BM(p, S, 1)
    print("Алгоритм Карпа-Рабина")
    KR(p, S, 2)
