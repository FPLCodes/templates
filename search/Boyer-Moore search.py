def bad_character_table(pattern):
    bad_char = [-1] * 256
    for i in range(len(pattern)):
        bad_char[ord(pattern[i])] = i
    return bad_char


def good_suffix_table_simple(pattern):
    m = len(pattern)
    suffix = [m] * m
    last_prefix_position = m

    for i in reversed(range(m - 1)):
        if is_prefix(pattern, i + 1):
            last_prefix_position = i + 1
        suffix[m - 1 - i] = last_prefix_position - i + m - 1

    return suffix


def is_prefix(pattern, p):
    m = len(pattern)
    for i in range(p, m):
        if pattern[i] != pattern[m - 1 - i + p]:
            return False
    return True


def full_shift_table_simple(pattern):
    m = len(pattern)
    good_suffix = good_suffix_table_simple(pattern)
    shift = [m] * m
    j = 0

    for i in range(m - 1):
        j = m - 1 - good_suffix[i]
        if shift[j] == m:
            shift[j] = i

    return shift


def boyer_moore_search(text, pattern):
    bad_char = bad_character_table(pattern)
    good_suffix = full_shift_table_simple(pattern)
    m = len(pattern)
    n = len(text)
    i = 0

    while i <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        if j < 0:
            yield i
            i += good_suffix[0] if m < n - i else 1
        else:
            i += max(good_suffix[j], j - bad_char[ord(text[i + j])])


# Example usage
text = "HERE IS A SIMPLE EXAMPLE"
pattern = "EXAMPLE"
matches = list(boyer_moore_search(text, pattern))
print("Pattern found at positions:", matches)
