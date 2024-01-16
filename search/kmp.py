def KMPSearch(pat, s):
    N, M = len(s), len(pat)

    lps = [0] * M
    compute_LPS_array(pat, M, lps)

    i = j = 0
    res = []
    while (N - i) >= (M - j):
        if pat[j] == s[i]:
            i += 1
            j += 1

        if j == M:
            res.append(i - j)
            j = lps[j - 1]

        elif i < N and pat[j] != s[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return res


def compute_LPS_array(pat, M, lps):
    plen = 0
    i = 1
    while i < M:
        if pat[i] == pat[plen]:
            plen += 1
            lps[i] = plen
            i += 1
        else:
            if plen != 0:
                plen = lps[plen - 1]
            else:
                lps[i] = 0
                i += 1
