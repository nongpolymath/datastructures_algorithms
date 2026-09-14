"""
Check Subtree: T1 and T2 are two very large binary trees, with T1 much bigger than T2. 
Create an algorithm to determine if T2 is a subtree of T1. 
A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2. 
That is, if you cut off the tree at node n, the two trees would be identical.
"""
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

    def same_tree(p, q):
        if not p and not q:
            return True
        if (p and not q) or (q and not p):
            return False
        if p.val != q.val:
            return False
        return same_tree(p.left , q.left) or same_tree(p.right, q.right)

    def has_subtree(root):
        if not root:
            return False
        if same_tree(root, subRoot):
            return True
        return has_subtree(root.left) or has_subtree(root.right)
    return has_subtree(root)