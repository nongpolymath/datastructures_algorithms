class BinaryTree:
    def __init__(self, size):
        self.items = size*[None]
        self.max_size = size
        self.last_used_index = 0

    def insert(self, value):
        if self.last_used_index+1 >= self.max_size:
            return False
        
        self.last_used_index +=1
        self.items[self.last_used_index]=value
        return True

    def search_node(self, value):
        """
        uses level order traversal
        """
        for i in range(1,self.last_used_index+1):
            if self.items[i] == value:
                return True
        return False
    
    def pre_order_traversal(self, index):
        if index > self.last_used_index:
            return
        print(self.items[index])
        self.pre_order_traversal(2*index)
        self.pre_order_traversal(index*2+1)

    def in_order_traversal(self, index):
        if index > self.last_used_index:
            return
        self.in_order_traversal(2*index)
        print(self.items[index])
        self.in_order_traversal(2*index+1)
        
    def post_order_traversal(self, index):
        if index > self.last_used_index:
            return
        self.post_order_traversal(2*index)
        self.post_order_traversal(2*index+1)
        print(self.items[index])

    def level_order_traversal(self):
        for i in range(1, self.last_used_index+1):
            print(self.items[i])

    # find deeepest node
    # replace value with deepest node
    # delete deepest node
    def delete_node(self, value):
        if self.last_used_index == 0:
            return False
        for i in range(1,self.last_used_index+1):
            if self.items[i] == value:
                self.items[i] == self.items[self.last_used_index]
                self.items[self.last_used_index] = None
                self.last_used_index -=1
                return True
        return False

    def delete_binary_tree(self):
        self.items = None
        self.last_used_index =0


newBT = BinaryTree(8)
newBT.insert("Drinks")
newBT.insert("Hot")
newBT.insert("Cold")
newBT.insert("Tea")
newBT.insert("Coffee")
print("----pre order traversal----")
newBT.pre_order_traversal(1)
print("----in order traversal----")
newBT.in_order_traversal(1)
print("----post order traversal----")
newBT.post_order_traversal(1)