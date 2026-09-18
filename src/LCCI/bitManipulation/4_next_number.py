"""
Next Number: Given a positive integer, print the next smallest and the next largest number that have the same number of 1 bits 
in their binary representation.
"""
def get_next_bigger(n: int) -> int:
    c = n
    c0 = c1 = 0
    while c & 1 == 0 and c !=0:
        c0 += 1
        c= c >> 1
    while c & 1 == 1:
        c1 += 1
        c = c >> 1
    if c0 + c1 ==31 or c0+c1 == 0:
        return -1
    pos = c0 + c1
    n = n | (1 << pos)
    n = n & ~((1<<pos)-1)
    n = n | (1<<(c1-1)) -1
    return n

def get_next_smaller(n: int) -> int:
    c = n
    c1 = c0 = 0

    # count trailing ones
    while c & 1 == 1:
        c1 += 1
        c >>= 1

    # edge case: n == 0
    if c == 0:
        return -1

    # count zeros right after those ones
    while c & 1 == 0 and c != 0:
        c0 += 1
        c >>= 1

    pos = c1 + c0                 # rightmost non-trailing one
    n &= ~((1 << (pos + 1)) - 1)  # clear bits from pos downward

    mask = (1 << (c1 + 1)) - 1    # (c1 + 1) ones
    n |= mask << (c0 - 1)         # place right-justified below pos

    return n
