"""
BST Sequences: A binary search tree was created by traversing through an array from left to right and inserting each element. 
Given a binary search tree with distinct elements, print all possible arrays that could have led to this tree.
"""

from math import comb
from typing import List

def numOfWays(nums: List[int]) -> int:
    MOD = 10**9 + 7

    def count_ways(arr):
        if len(arr) <=2 :
            return 1
        root = arr[0]
        left = [x for x in arr if x < root]
        right = [x for x in arr if x > root]
        ways = comb(len(left + right), len(left))
        return (ways * count_ways(left) * count_ways(right)) % MOD
    return count_ways(nums) % MOD