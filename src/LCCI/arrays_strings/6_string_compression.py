# Implement a method to perform basic string compression using the counts of repeated characters. 
# For example, the string aabcccccaaa would become a2b1c5a3. 
# If the compressed string would not become smaller than the original string, 
# your method should return the original string. 
# You can assume the string has only uppercase and lowercase letters (a-z).

def compress(s: str):
    if not s: return s
    res = []
    count = 1
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            count +=1
        else: 
            res.append(s[i-1]+ str(count))
            count = 1  
    res.append(s[-1] + str(count))
    comp = ''.join(res)
    return comp if len(comp) < len(s) else s


# test harness 
if __name__ == "__main__":
    test_cases = [
        ("aabcccccaaa", "a2b1c5a3"),   # standard case from the prompt
        ("abcdef", "abcdef"),          # no repeats -> compressed longer, return original
        ("", ""),                     # empty string
        ("a", "a"),                    # single char -> "a1" is longer, return original
        ("aa", "aa"),                  # tie in length -> return original
        ("aaaa", "a4"),                 # clear win for compression
        ("aabbcc", "aabbcc"),           # "a2b2c2" is same length as original -> return original
    ]

    passed = 0
    for s, expected in test_cases:
        actual = compress(s)
        status = "PASS" if actual == expected else "FAIL"
        if status == "PASS":
            passed += 1
        print(f"{status}: compress({s!r}) = {actual!r} (expected {expected!r})")

    print(f"\n{passed}/{len(test_cases)} tests passed")