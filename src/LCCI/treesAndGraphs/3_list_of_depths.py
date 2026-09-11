"""
List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth 
(e.g., if you have a tree with depth 0, you'll have 0 linked lists).
"""
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Node:
    def __init__(self , val=None):
        self.val = val
        self.next = None

def list_of_depths(root):
    if not root:
        return [None]
    q = deque()
    q.append(root)
    res = []

    while q:
        dummy = Node()
        curr = dummy
        lvl_len = len(q)
        for _ in range(lvl_len):
            n = q.popleft()
            node = Node(n.val)
            curr.next = node
            curr = node
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        curr.next = None
        res.append(dummy.next)
    return res