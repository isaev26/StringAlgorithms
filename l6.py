def Shift_And(P, T):
    m = len(P)
    n = len(T)

    B = {}
    for i in range(m):
        B[P[i]] = (B.get(P[i], 0) | (1 << i))

    M = 0
    for i in range(n):
        M = ((M << 1) | 1) & (B.get(T[i], 0))

        if M & (1 << (m - 1)):
            print("Вхождение с позиции %d" % (i - m + 1))


def Shift_And_Fz(p, t, k):
    m, n = len(p), len(t)
    ch_beg, ch_end = '0', 'z'
    nA = ord(ch_end) - ord(ch_beg) + 1
    B = [0] * nA
    for j in range(m):
        B[ord(p[j]) - ord(ch_beg)] |= 1 << m - 1 - j
    u_high = 1 << (m - 1)
    M = [0] * (k + 1)
    M1 = [0] * (k + 1)
    for i in range(n):
        for l in range(k + 1):
            M1[l] = M[l]
            M[l] = (M[l] >> 1 | u_high) & B[ord(t[i]) - ord(ch_beg)]
            if l:
                M[l] |= M1[l - 1] >> 1 | u_high
            if l == k and M[l] & 1:
                print("Найдено вхождение ", i - m + 1)


if __name__ == "__main__":
    with open("text.txt", "r") as file:
        T = file.readline()
        print("String-> " + T)
        n = len(T)

        P = input("Введите подстроку: ")

        print("Алгоритм Shift-And")
        Shift_And(P, T)
        print("Алгоритм Shift-And-Fz")
        k = int(input("Введите k "))
        while k >= len(P):
            k = int(input("k должно быть меньше длины подстроки "))
        Shift_And_Fz(P, T, k)
