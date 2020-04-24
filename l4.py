def Prefix_Border_Array(S):
    n = len(S)
    bp = [0]

    for i in range(1, n):
        bpRight = bp[i - 1]
        while bpRight and S[i] != S[bpRight]:
            bpRight = bp[bpRight - 1]
        if S[i] == S[bpRight]:
            bp.append(bpRight + 1)
        else:
            bp.append(0)

    return bp


def BP_to_BPM(bp, n):
    bpm = [0]*n
    bpm[n-1] = bp[n-1]
    for i in range(1, n-1):
        if(bp[i] and (bp[i]+1 == bp[i+1])):
            bpm[i] = bpm[bp[i]-1]
        else:
            bpm[i] = bp[i]

    return bpm
# ########################################################


def kmp(p, t):
    m = len(p)
    n = len(t)
    #  Текущий индекс в образце
    k = 0
    # Модифицированный массив граней
    p_bpm = BP_to_BPM(Prefix_Border_Array(p), m)
    for i in range(n):
        while k and p[k] != t[i]:
            k = p_bpm[k - 1]
        if p[k] == t[i]:
            k += 1
        if k == m:
            print("Вхождение с позиции", i - k + 1)
            k = p_bpm[k - 1]


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


def BM(p, t):
    pl = position_list(p)
    m, n = len(p), len(t)
    n_text_r = m
    while n_text_r <= n:
        i = n_text_r - 1
        k = m - 1
        while k >= 0 and p[k] == t[i]:
            k -= 1
            i -= 1
        if k < 0:
            print("Вхождение с позиции", i + 1)
        n_text_r += bad_char_shift(pl, t[i], k)


if __name__ == '__main__':
    with open("text.txt", "r") as file:
        S = file.readline()
        print("String-> " + S)
        n = len(S)

    p = input("Введите подстроку: ")
    print("KMP")
    kmp(p, S)
    print("BM")
    BM(p, S)
