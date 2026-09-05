# Implement an algorithm to determine if a string has all unique characters.
# Second : what if you cannot use extra data structures? 

# using hash set o(N)
def is_unique(s: str) -> bool:
    seen = set()
    for ch in s:
        if ch in seen:
            return False
        seen.add(ch)
    return True

# using sorted array o(logN)
def is_unique_sorted(s: str) -> bool:
    chars = sorted(s)
    for i in range(len(chars) - 1):
        if chars[i] == chars[i+1]:
            return False
    return True

# using bit masking
def is_unique_bitmask(s: str) -> bool:
    checker = 0
    for char in s:
        val = ord(char) - ord('a')
        if checker & (1<<val):
            return False
        checker |= (1<<val)
    return True


if __name__ == "__main__":
    test_cases = ["abcdefg", "hello", "", "a", "Aa"]
    funcs = [is_unique, is_unique_sorted, is_unique_bitmask]

    for s in test_cases:
        print(f"{s!r}", end=": ")
        for f in funcs:
            try:
                print(f.__name__, "=", f(s), end="  ")
            except Exception as e:
                print(f.__name__, "= ERROR", end="  ")
        print()