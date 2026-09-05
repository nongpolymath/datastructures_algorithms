# One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, 
# or replace a character. Given two strings, write a function to check if they are one edit or zero edits away

def is_one_edit_distance(s: str, t: str) -> bool:
    if abs(len(s) - len(t)) > 1 :
        return False
    m = 0
    i = j = 0
    shorter , longer = (t, s) if len(t) < len(s) else (s, t)
    while i < len(shorter) and j < len(longer):
        if shorter[i] != longer[j]:
            m += 1
            j += 1
            if len(shorter) == len(longer):
                i += 1
        else:
            i += 1
            j += 1
    return m < 2

# test harness
if __name__ == "__main__":
    test_cases = [
        ("", "", True),
        ("a", "a", True),
        ("pale", "bale", True),      # replace at front
        ("pale", "palf", True),      # replace at end
        ("pale", "ple", True),       # remove middle char
        ("ple", "pale", True),       # insert middle char
        ("", "a", True),             # insert into empty string
        ("ab", "xab", True),         # insert at front
        ("pale", "bake", False),     # two replaces
        ("abc", "axyc", False),      # two inserts
        ("a", "abcd", False),        # length differs by 3
    ]
 
    passed = 0
    for s, t, expected in test_cases:
        got = is_one_edit_distance(s, t)
        status = "PASS" if got == expected else "FAIL"
        passed += got == expected
        print(f"[{status}] is_one_edit_distance({s!r}, {t!r}) -> {got} (expected {expected})")
 
    print(f"\n{passed}/{len(test_cases)} tests passed")