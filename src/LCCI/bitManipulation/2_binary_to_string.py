"""
Binary to String: Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a double, print the binary representation. 
If the number cannot be represented accurately in binary with at most 32 characters, print "ERROR:"
"""

def binary_to_string(num: float) -> str:
    if num <= 0 or num >1:
        return "ERROR:"
    binary = "0."
    while num > 0:
        if len(binary) >32:
            return "ERROR:"
        num *=2
        if num >= 1:
            binary += '1'
            num -= 1
        else:
            binary += '0'

    return binary


