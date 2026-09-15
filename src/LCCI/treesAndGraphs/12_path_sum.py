"""
Paths with Sum: You are given a binary tree in which each node contains an integer value (which might be positive or negative). 
Design an algorithm to count the number of paths that sum to a given value. 
The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import defaultdict

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1
        answer = [0]
        def dfs(node, running_sum):
            if not node:
                return
            running_sum += node.val
            answer[0] += prefix_counts[running_sum - targetSum]
            prefix_counts[running_sum] +=1
            dfs(node.left, running_sum)
            dfs(node.right, running_sum)
            prefix_counts[running_sum] -= 1 # backtrack
        
        dfs(root, 0)
        return answer[0]