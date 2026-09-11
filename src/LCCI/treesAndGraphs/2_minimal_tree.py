"""
Minimal Tree: Given a sorted (increasing order) array with unique integer elements, 
write an algorithm to create a binary search tree with minimal height.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """

        def bst(l, r):
            if l > r:
                return None
            m = (l + r)//2
            root = TreeNode(nums[m])
            root.left = bst(l , m-1)
            root.right = bst(m+1 , r)
            return root
        return bst(0 , len(nums) - 1)