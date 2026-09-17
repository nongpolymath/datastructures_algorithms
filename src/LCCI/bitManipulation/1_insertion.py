"""
Insertion: You are given two 32-bit numbers, N and M, and two bit positions, i and j. Write a method to insert M into N such that M starts at bit j 
and ends at bit i. You can assume that the bits j through i have enough space to fit all of M. 
That is, if M = 10011, you can assume that there are at least 5 bits between j and i. 
You would not, for example, have j = 3 and i = 2, because M could not fully fit between bit 3 and bit 2. 
EXAMPLE Input: N = 10000000000, M = 10011, i = 2, j = 6 Output: N 10001001100
"""
def insertion(N, M, i , j):
    all_ones = ~0         # 111111111 ....
    left = all_ones << j+1
    right = (1<< i) - 1
    mask = left | right
    n_mask = N & mask
    m_shifted = M << i

    result = n_mask | m_shifted
    return result





def test_insertion():
    # Example from the problem statement
    N = int("10000000000", 2)
    M = int("10011", 2)
    i, j = 2, 6
    expected = int("10001001100", 2)
    assert insertion(N, M, i, j) == expected, "Example case failed"

    # M fills the entire range exactly (i=0)
    N = int("00000000", 2)
    M = int("1111", 2)
    i, j = 0, 3
    expected = int("00001111", 2)
    assert insertion(N, M, i, j) == expected, "Full-range insert failed"

    # Insert into the middle, N has bits on both sides of the insertion window
    N = int("11111111", 2)
    M = int("0000", 2)
    i, j = 2, 5
    expected = int("11000011", 2)
    assert insertion(N, M, i, j) == expected, "Clearing bits with zero M failed"

    # Single-bit insert
    N = int("10101010", 2)
    M = int("1", 2)
    i, j = 3, 3
    expected = int("10101010", 2)  # bit 3 was already 1, no visible change
    assert insertion(N, M, i, j) == expected, "Single-bit insert failed"

    # Single-bit insert that actually flips a bit
    N = int("10100010", 2)
    M = int("1", 2)
    i, j = 2, 2
    expected = int("10100110", 2)
    assert insertion(N, M, i, j) == expected, "Single-bit flip failed"

    print("All tests passed!")


if __name__ == "__main__":
    test_insertion()