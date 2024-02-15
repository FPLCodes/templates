def calculate_z_array(string):
    n = len(string)
    z = [0] * n
    l, r = 0, 0

    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])

        while i + z[i] < n and string[z[i]] == string[i + z[i]]:
            z[i] += 1

        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1

    return z


def z_algorithm(text, pattern):
    concat = pattern + "$" + text
    z_array = calculate_z_array(concat)
    pattern_length = len(pattern)
    matches = []

    for i in range(pattern_length + 1, len(concat)):
        if z_array[i] == pattern_length:
            matches.append(i - pattern_length - 1)

    return matches


# Example usage
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
matches = z_algorithm(text, pattern)
print("Pattern found at positions:", matches)
