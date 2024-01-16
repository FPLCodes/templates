from collections import Counter, defaultdict


def ArrayChallenge(strArr):
    s, words = strArr[0], strArr[1].split(",")
    d, res = Counter(s), []
    for word in words:
        if len(res) == 2:
            break

        curr, valid = defaultdict(int), True
        for c in word:
            curr[c] += 1
            if not (c in d and curr[c] <= d[c]):
                valid = False
                break
        if valid:
            res.append(word)

    return ",".join(res) if len(res) == 2 else "not possible"


print(ArrayChallenge(["hellocat", "apple,bat,cat,goodbye,hello,yellow,why"]))
