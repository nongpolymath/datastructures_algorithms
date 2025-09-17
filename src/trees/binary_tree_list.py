class BinaryTree:
    def __init__(self, size):
        self.tree = size *[None]
        self.max_size = size
        self.last_used_index = 0

    def insert(self, value):
        if self.last_used_index +1 == self.max_size:
            return "Binary Tree is Full"
        self.last_used_index+=1
        self.tree[self.last_used_index] = value
        return "node inserted to Binary Tree"
    
    def search_bst(self, value):
        """search for node using Level order traversal
        Args:
            value (_type_): _description_
        """
        if self.last_used_index == 0:
            return "empty Binary Tree"
        
        for i in range(self.last_used_index):
            if self.tree[i] == value:
                return "Node found"
        return "Node not found"

    def preorder_traversal(self, index):
        if index >self.last_used_index:
            return
        print(self.tree[index])
        self.preorder_traversal(2*index)
        self.preorder_traversal(2*index+1)
        
    def inorder_traversal(self, index):
        if index >self.last_used_index:
            return
        self.inorder_traversal(2*index)
        print(self.tree[index])
        self.inorder_traversal(2*index+1)
        
    def postorder_traversal(self, index):
        if index >self.last_used_index:
            return
        self.postorder_traversal(index*2)
        self.postorder_traversal(index*2+1)
        print(self.tree[index])
        
    def levelorder_traversal(self,index):
        for i in range(index, self.last_used_index+1):
            print(self.tree[i])
    
    def delete_node(self, node):
        if node >self.last_used_index:
            return False
        for i in range(1,self.last_used_index+1):
            if self.tree[i] == node:
                self.tree[i] = self.tree[self.last_used_index]
                self.tree[self.last_used_index] = None
                self.last_used_index-=1
                return True
            return False
        
    def delete_tree(self):
        self.tree = None
        

newBT = BinaryTree(8)
newBT.insert("Drinks")
newBT.insert("Hot")
newBT.insert("Cold")
newBT.insert("Tea")
newBT.insert("Coffee")

newBT.postorder_traversal(1)
newBT.delete_node('Coffee')