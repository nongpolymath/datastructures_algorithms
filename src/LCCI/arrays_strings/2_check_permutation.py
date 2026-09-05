# Given two strings , Write a method to decide if one is a permutation of the other

def is_permutation_sorted(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)


def is_permutation_count(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    s1_count , s2_count = {} , {}
    for ch in s1:
        s1_count[ch] = 1 + s1_count.get(ch, 0)
    for c in s2:
        s2_count[c] = 1 + s2_count.get(c, 0)
    return s1_count == s2_count


if __name__ == "__main__":
    test_cases = [
        ("abc", "cba"),      # True - simple permutation
        ("abc", "abcd"),     # False - different lengths
        ("", ""),            # True - empty strings
        ("aabbcc", "abcabc"),# True - repeated chars
        ("abc", "abd"),      # False - same length, different chars
    ]
    funcs = [is_permutation_sorted, is_permutation_count]

    for s1, s2 in test_cases:
        print(f"{s1!r}, {s2!r}", end=": ")
        for f in funcs:
            print(f.__name__, "=", f(s1, s2), end="  ")
        print()