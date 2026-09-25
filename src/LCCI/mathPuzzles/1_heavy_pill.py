"""
The Heavy Pill: You have 20 bottles of pills. 19 bottles have 1.0 gram pills, but one has pills of weight 1.1 grams. 
Given a scale that provides an exact measurement, how would you find the heavy bottle? You can only use the scale once.

The core idea is to make the single measurement carry enough information to identify the culprit. One weighing can't compare bottles directly, so you encode each bottle's identity into the total by taking a different number of pills from each one.

The solution
1. Take 1 pill from bottle 1, 2 pills from bottle 2, and so on up to 20 pills from bottle 20. That is 1 + 2 + ... + 20 = 210 pills.
2. If every pill weighed 1.0 g, the scale would read exactly 210.0 g.
3. Every pill from the heavy bottle carries an extra 0.1 g. Bottle N contributes N pills, so the excess is N × 0.1 g.
4. Divide the excess by 0.1 to get N.
"""

def find_heavy(scale_reading: float, n: int = 20, delta: float = 0.1) -> int:
    expected = n * (n + 1) / 2          # all pills 1.0 g
    return round((scale_reading - expected) / delta)



"""
Leetcode 458. Poor Pigs
states = rounds + 1, one pig distinguishes states buckets
p pigs can distinguish states^p buckets.
The problem reduces to:
Find the smallest p such that states^p >= buckets.

"""

def poorPigs(buckets: int, minutesToDie: int, minutesToTest: int) -> int:
    rounds = minutesToTest // minutesToDie # how many rounds can a pig go without dying
    states = rounds + 1 # different states a bucket can be identified by 1 pig
    pigs = 0
    while states ** pigs < buckets:
        pigs +=1
    return pigs