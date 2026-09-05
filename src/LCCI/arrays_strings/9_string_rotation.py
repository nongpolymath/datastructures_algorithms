'''
String Rotation: Assume you have a method isSubstring which checks if one word is a substring of another. 
Given two strings, S1 and S2, write code to check if S2 is a rotation of S1 using only one call 
to isSubstring (e.g., "waterbottle" is a rotation of "erbottlewat").
'''

def isSubstring(s1: str, s2: str) -> bool:
    return s2 in s1

def is_rotation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2) or len(s1) == 0 or len(s2) == 0:
        return False
    return isSubstring(s1+s1, s2)

if __name__ == "__main__":
    cases = [
        ("waterbottle", "erbottlewat", True),   # CTCI example
        ("abcde", "cdeab", True),               # rotation
        ("abcde", "abced", False),              # same length, not a rotation
        ("abc", "ab", False),                   # different lengths
        ("", "", False),                        # empty strings
        ("a", "a", True),                       # single char, trivial rotation
        ("ab", "ba", True),                     # rotation by 1
    ]
 
    for s1, s2, expected in cases:
        result = is_rotation(s1, s2)
        assert result == expected, f"is_rotation({s1!r}, {s2!r}) = {result}, expected {expected}"
 
    print("all tests passed")