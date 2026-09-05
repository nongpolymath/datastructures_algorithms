# Given a string write a function to check if it is a permutation of a palindrome . A palindrome is a word or phrase that is the same forwards and backwards . 
# A permutation is a rearrangement of letters .
# The palindrome does not need to be limited to just dictionary words. You can ignore casing and non - letter words .

def can_permute_palindrome(s: str) -> bool:
    odd_chars = set()
    for ch in s:
        if not ch.isalpha():
            continue
        ch = ch.lower()

        if ch in odd_chars:
            odd_chars.remove(ch)
        else:
            odd_chars.add(ch)
    return len(odd_chars) <= 1

# test harness
if __name__ == "__main__":
    tests = [
        ("Tact Coa", True),                    # -> "taco cat"
        ("civic", True),
        ("ivicc", True),
        ("hello", False),
        ("aab", True),
        ("carerac", True),
        ("", True),
        ("a", True),
        ("Able was I ere I saw Elba", True),
        ("This is not a palindrome", False),
        ("A man a plan a canal Panama", True),
    ]

    for s, expected in tests:
        result = can_permute_palindrome(s)
        status = "OK" if result == expected else "FAIL"
        print(f"{s!r:35} -> {result!s:5} [{status}]")
