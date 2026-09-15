"""
Random Node: You are implementing a binary tree class from scratch which, in addition to insert, find, and delete,
has a method getRandomNode() which returns a random node from the tree. All nodes should be equally likely to be chosen. 
Design and implement an algorithm for getRandomNode, and explain how you would implement the rest of the methods.
"""
class Node:
    def __init__(self , val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self , root = None):
        self.root = root

    def insert(self, val):
        self._insert(self.root, val)
    
    def _insert(self, node, val):
        if node is None:
            return Node(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        else:
            node.right = self._insert(node.right, val)
        return node

    def find(self, val):
        return self._find(self.root, val)
 
    def _find(self, node, val):
        if node is None or node.val == val:
            return node
        if val < node.left.val:
            self._find(node.left, val)
        else:
            self._find(node.right, val)


    def delete(self, key):
        return self._delete(self.root , key)


    def _delete(self, root , key):
        if root is None:
            return None
        if key < root.val:
            root.left = self._delete(root.left , key)
        elif key > root.val:
            root.right = self._delete(root.right, key)
        else:
            if not root.left:
                return root.right
            else:
                if not root.right:
                    return root.left
            s = root.right
            while s.left:
                s = s.left
            root.val = s.val
            root.right = self._delete(root.right, s.val)
        return root