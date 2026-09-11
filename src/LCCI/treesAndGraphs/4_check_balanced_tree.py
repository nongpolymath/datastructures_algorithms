"""
Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of this question, 
a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one.
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        balanced = [True]

        def height(node):
            if not node:
                return 0
            height_left = height(node.left)
            if balanced[0] is False:
                return 0
            height_right = height(node.right)
            if abs(height_left - height_right) > 1:
                balanced[0] = False
                return 0
            return 1 + max(height_left , height_right)
        height(root)
        return balanced[0]