"""
Validate BST: Implement a function to check if a binary tree is a binary search tree.
"""

# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def is_valid(node, min, max):
            if not node:
                return True
            if node.val >= max or node.val <= min:
                return False
            return is_valid(node.left, min , node.val) and is_valid(node.right, node.val, max)

        is_valid(root, float('-inf') , float('inf'))