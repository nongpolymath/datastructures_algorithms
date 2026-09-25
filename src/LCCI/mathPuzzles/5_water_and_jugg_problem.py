"""
Jugs of Water: You have a five-quart jug, a three-quart jug, and an unlimited supply of water (but no measuring cups). 
How would you come up with exactly four quarts of water? 
Note that the jugs are oddly shaped, such that filling up exactly "half" of the jug would be impossible.
"""

def canMeasureWater(x: int, y: int, target: int) -> bool:
    if target > x + y : 
        return False
    if x > y:
        x , y = y , x
    return target % gcd(x, y)

def gcd(a, b):
    while b:
        a , b = b , b % a
    return a