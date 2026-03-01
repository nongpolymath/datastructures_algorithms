from queues_lib.queue_linked_list import LinkedListQueue

class BSTNode:
    def __init__(self, value = None):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_node(self, root_node, node_value):
        if not root_node:
            return BSTNode(node_value)
        if node_value < root_node.value:
            root_node.left_child = self.insert_node(root_node.left_child,node_value)
        else:
            root_node.right_child = self.insert_node(root_node.right_child, node_value)
        return root_node

    def pre_order_traversal(self, root_node):
        if not root_node:
            return
        print(root_node.value)
        self.pre_order_traversal(root_node.left_child)
        self.pre_order_traversal(root_node.right_child)

    def inorder_traversal(self, root_node):
        if not root_node:
            return
        self.inorder_traversal(root_node.left_child)
        print(root_node.value)
        self.inorder_traversal(root_node.right_child)

    def post_order_traversal(self, root_node):
        if not root_node:
            return
        self.post_order_traversal(root_node.left_child)
        self.post_order_traversal(root_node.right_child)
        print(root_node.value)

    def level_order_traversal(self, root_node):
        if not root_node:
            return None
        new_queue = LinkedListQueue()
        new_queue.enqueue(root_node)
        while new_queue.front is not None:
            current_node = new_queue.dequeue()
            print(current_node.value.value)
            if current_node.value.left_child:
                new_queue.enqueue(current_node.value.left_child)
            if current_node.value.right_child:
                new_queue.enqueue(current_node.value.right_child)

    def search_node(self, root_node, search_value):
        if not root_node:
            return None
        current = root_node
        if current.value == search_value:
            return current
        if current.value>search_value:
            return self.search_node(current.left_child, search_value)
        else:
            return self.search_node(current.right_child, search_value)
        

    def search_node_level_order(self, root_node, search_value):
        if root_node.value == search_value:
            return True
        new_queue = LinkedListQueue()
        new_queue.enqueue(root_node)
        while new_queue.front is not None:
            current_node = new_queue.dequeue()
            if current_node.value.value == search_value:
                return True
            if current_node.value.left_child:
                new_queue.enqueue(current_node.value.left_child)
            if current_node.value.right_child:
                new_queue.enqueue(current_node.value.right_child)
        return False

    def find_min_node(self, root_node):
        current = root_node
        while current.left_child:
            current = current.left_child
        return current
    
    def delete_node(self, root, key):
        if root is None:
            return root
        # step 1 find the node:
        if key < root.value:
            root.left_child = self.delete_node(root.left_child, key)
        elif key > root.value:
            root.right_child = self.delete_node(root.right_child, key)
        else:
            # step 2 node found
            # case 1 no child node 1 child node
            if root.left_child is None:
                return root.right_child
            elif root.right_child is None:
                return root.left_child
            # in order successor of the right sub tree
            temp = self.find_min_node(root.right_child)
            root.value = temp.value
            root.right_child = self.delete_node(root, temp.value)
        return root

    def delete_bst(self, root):
        root.data = None
        root.left_Child = None
        root.right_child = None

# # slightly different recursive approach to insert tree 
# def insert_node_bst(root_node, node_value):
#     if root_node is None:
#         return BSTNode(node_value)
#     else:
#         if node_value <= root_node.value:
#             if root_node.left_child is None:
#                 root_node.left_child = BSTNode(node_value)
#             else:
#                 insert_node_bst(root_node.left_child, node_value)
                
#         else:
#             if root_node.right_child is None:
#                 root_node.right_child = BSTNode(node_value)
#             else:
#                 insert_node_bst(root_node.right_child, node_value)      # o(logN) time complexity
#     return root_node

    def delete_node_bst(self, root, key):
        if root is None:
            return root
        



newBST = BSTNode(None)
root = None
root = newBST.insert_node(root,70)
root = newBST.insert_node(root, 50)
root = newBST.insert_node(root, 90)
root = newBST.insert_node(root, 30)
root = newBST.insert_node(root, 60)
root = newBST.insert_node(root, 80)
root = newBST.insert_node(root, 100)
root = newBST.insert_node(root, 20)
root = newBST.insert_node(root, 40)
print("----pre order traversal----")
newBST.pre_order_traversal(root)
print("----in order traversal")
newBST.inorder_traversal(root)
print("----post order traversal")
newBST.post_order_traversal(root)
print("----level order traversal----")
newBST.level_order_traversal(root)
node = newBST.search_node(root, 60)
print(f"Node found for search value {node.value}")
print(newBST.search_node_level_order(root, 150))