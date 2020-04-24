def native_max_border(S):
    n = len(S)
    br = [0]

    for i in range(n-1):
        j = 0
        while (j < i) and S[j] == S[n-i+j]:
            j += 1
        if j == i:
            br = i

    return br


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


def Prefix_Border_ArrayM(S, bp):
    n = len(S)
    bpm = [0]*n
    bpm[n-1] = bp[n-1]

    for i in range(1, n-1):
        if bp[i] and (S[bp[i]] == S[i+1]):
            bpm[i] = bpm[bp[i] - 1]
        else:
            bpm[i] = bp[i]

    return bpm


def BP_to_BPM(bp, n):
    bpm = [0]*n
    bpm[n-1] = bp[n-1]
    for i in range(1, n-1):
        if(bp[i] and (bp[i]+1 == bp[i+1])):
            bpm[i] = bpm[bp[i]-1]
        else:
            bpm[i] = bp[i]

    return bpm


def BPM_to_BP(bpm, n):
    bp[n-1] = bpm[n-1]
    bp[0] = 0
    for i in range(n-2, 0, -1):
        bp[i] = max(bp[i+1]-1, bpm[i])

    return bp


def BS_to_BSM(bs, n):
    bsm = [0]*n
    bsm[0] = bs[0]
    for i in range(n-2, 0, -1):
        if(bs[i]and (bs[i]+1 == bs[i-1])):
            bsm[i] = bsm[n-bs[i]]
        else:
            bsm[i] = bs[i]
    return bsm


def BSM_to_BS(bsm, n):
    bs = [0]*n
    bs[0] = bsm[0]
    for i in range(1, n-1):
        bs[i] = max(bs[i-1]-1, bsm[i])

    return bs


if __name__ == "__main__":
    with open("text.txt", "r") as file:
        S = file.readline()
        print("String-> " + S)
        n = len(S)

print("Наибольшая грань:")
br = native_max_border(S)
print(br)

print("Массив граней:")
bp = Prefix_Border_Array(S)
print(bp)

print("Массив граней суффиксов:")
bs = Suffix_Border_Array(S)
print(bs)

print("Массив граней суффиксов мод.:")
bpm = Prefix_Border_ArrayM(S, bp)
print(bpm)

print("Преобразование bp в bpm без S:")
bp_to_bpm = BP_to_BPM(bp, n)
print(bp_to_bpm)

print("Преобразование bpm в bp:")
bpm_to_bp = BPM_to_BP(bpm, n)
print(bpm_to_bp)

print("Преобразование bs в bsm:")
bsm = BS_to_BSM(bs, n)
print(bsm)

print("Преобразование bsm в bs:")
bsm_to_bs = BSM_to_BS(bsm, n)
print(bsm_to_bs)
