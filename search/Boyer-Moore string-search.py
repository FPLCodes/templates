def boyer_moore_search(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return []

    # Preprocess the pattern
    last_occurrence = {}
    for i in range(m):
        last_occurrence[pattern[i]] = i

    # Search for the pattern in the text
    i = m - 1
    j = m - 1
    occurrences = []
    while i < n:
        if text[i] == pattern[j]:
            if j == 0:
                occurrences.append(i)
                i += m
                j = m - 1
            else:
                i -= 1
                j -= 1
        else:
            if text[i] in last_occurrence:
                i += m - min(j, 1 + last_occurrence[text[i]])
            else:
                i += m
            j = m - 1

    return occurrences
