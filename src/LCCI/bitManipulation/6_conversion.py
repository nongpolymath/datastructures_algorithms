"""
Conversion: Write a function to determine the number of bits you would need to flip to convert integer A to integer B.
 EXAMPLE Input: 29 ( or: 111101 ), 15 ( or: 01111) Output: 2
 Its another way of saying calculate the hamming distance
"""
def conversion_bits(x, y):
    z = x ^ y
    count = 0
    while z:
        z = z & (z-1)
        count +=1
    return count

