"""
Successor: Write an algorithm to find the "next" node (i .e., in-order successor) of a given node in a binary search tree.
 You may assume that each node has a link to its parent.
"""

# Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None


class Solution:
    """
    @param node: random node in binary search tree
    @return: the inorder successor of current node
    """
    def inorder_successor(self, node: ParentTreeNode) -> ParentTreeNode:
        # write your code here
        if node is None:
            return None

        # if right subtree exists , then find the leftmost node in the left subtree of node.right 
        if node.right:
            node = node.right
            while node.left:
                node = node.left
        # if node has no right subtree . climb through the node's parent (node is a right child of parent) until the node is a left child of the node's ancestor
        while node.parent and node  is node.parent.right:
            node = node.parent
        return node.parent