"""
Pairwise Swap: Write a program to swap odd and even bits in an integer with as few instructions as possible
(e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, and so on).
"""
def swap_pair(n: int):
    even_mask = 0x55555555  # 0b0101...0101
    odd_mask  = 0xAAAAAAAA  # 0b1010...1010

    evens = (n & even_mask) << 1   # move even bits up into odd slots
    odds  = (n & odd_mask) >> 1    # move odd bits down into even slots

    return evens | odds