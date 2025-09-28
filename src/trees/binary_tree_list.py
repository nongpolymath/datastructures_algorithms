class BinaryTree:
    """
    A Binary Tree implementation using a Python list (array).
    Nodes are stored in a level-order fashion.
    The root is at index 1. For any node at index `i`, its left child is at `2*i`
    and its right child is at `2*i + 1`.
    """
    def __init__(self, size):
        """
        Initializes a BinaryTree with a given maximum size.

        Args:
        size (int): The maximum number of nodes the tree can hold.
        """
        self.tree = size *[None]
        self.max_size = size
        self.last_used_index = 0

    def insert(self, value):
        """
         Inserts a new node with the given value into the binary tree.
         The insertion happens at the next available position in level order.

         Args:
         value: The data to be stored in the new node.

         Returns:
         str: A message indicating whether the insertion was successful or if the tree is full.
         """
        if self.last_used_index +1 == self.max_size:
            return "Binary Tree is Full"
        self.last_used_index+=1
        self.tree[self.last_used_index] = value
        return "node inserted to Binary Tree"
    
    def search_node(self, value):
        """
         Searches for a node with the given value in the binary tree using level-order traversal.

         Args:
         value: The value to search for.

         Returns:
         str: "Node found" if the value is present, "Node not found" otherwise,
         or "empty Binary Tree" if the tree is empty.
         """
        if self.last_used_index == 0:
            return "empty Binary Tree"
        
        # Start from index 1 as index 0 is unused
        for i in range(1, self.last_used_index + 1):
            if self.tree[i] == value:
                return "Node found"
        return "Node not found"

    def preorder_traversal(self, index):
        """Performs a pre-order traversal (Root -> Left -> Right) starting from the given index."""
        if index >self.last_used_index:
            return
        print(self.tree[index])
        self.preorder_traversal(2*index)
        self.preorder_traversal(2*index+1)
        
    def inorder_traversal(self, index):
        """Performs an in-order traversal (Left -> Root -> Right) starting from the given index."""
        if index >self.last_used_index:
            return
        self.inorder_traversal(2*index)
        print(self.tree[index])
        self.inorder_traversal(2*index+1)
        
    def postorder_traversal(self, index):
        """Performs a post-order traversal (Left -> Right -> Root) starting from the given index."""
        if index >self.last_used_index:
            return
        self.postorder_traversal(index*2)
        self.postorder_traversal(index*2+1)
        print(self.tree[index])
        
    def levelorder_traversal(self,index):
        """
        Performs a level-order traversal starting from the given index.
        This effectively prints all nodes from the given index to the last used index.
        """
        for i in range(index, self.last_used_index+1):
            print(self.tree[i])
    
    def delete_node(self, value):
        """
        Deletes a node with the given value from the binary tree.
        To maintain the complete binary tree structure, the node to be deleted
        is replaced by the deepest rightmost node, which is then removed.

         Args:
         value: The value of the node to be deleted.

         Returns:
         bool: True if the node was found and deleted, False otherwise.
         """
        if self.last_used_index == 0:
            return False # Tree is empty

        for i in range(1,self.last_used_index+1):
            if self.tree[i] == value:
                self.tree[i] = self.tree[self.last_used_index]
                self.tree[self.last_used_index] = None
                self.last_used_index-=1
                return True
        return False # Node not found after iterating
        
    def delete_tree(self):
        """
         Deletes the entire binary tree by setting the tree array to None
         and resetting the last used index.
        """
        self.tree = None
        self.last_used_index = 0
        

newBT = BinaryTree(8)
newBT.insert("Drinks")
newBT.insert("Hot")
newBT.insert("Cold")
newBT.insert("Tea")
newBT.insert("Coffee")

# Example usage:
# newBT.postorder_traversal(1)
# newBT.delete_node('Coffee')
# newBT.levelorder_traversal(1)
# print(newBT.search_node("Tea"))
# newBT.delete_tree()
# print(newBT.tree)