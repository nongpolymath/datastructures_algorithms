from queues_lib.queue_linked_list import LinkedListQueue

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        
    
def insert_node(root_node, node_value):
    if root_node.data is None:
        root_node.data = node_value
    else:
        if node_value <= root_node.data:
            if root_node.left_child is None:
                root_node.left_child = BSTNode(node_value)
            else:
                insert_node(root_node.left_child, node_value)
                
        else:
            if root_node.right_child is None:
                root_node.right_child = BSTNode(node_value)
            else:
                insert_node(root_node.right_child, node_value)      # o(logN) time complexity
    return root_node

#preorder traversal order is Root Node -> Left Subtree -> Right Subtree
def preorder_traversal_bst(root_node):
    if root_node is None:
        return
    print(root_node.data)
    preorder_traversal_bst(root_node.left_child)
    preorder_traversal_bst(root_node.right_child)         # Time complexity is o(N)

#inorder traversal order is Left Subtree -> Root Node -> Right Subtree
def inorder_traversal_bst(root_node):
    if root_node is None:
        return
    inorder_traversal_bst(root_node.left_child)
    print(root_node.data)
    inorder_traversal_bst(root_node.right_child)        # Time complexity is o(N)
    
#postorder traversal order is LEft Subtree -> Right Subtree -> Root node
def postorder_traversal_bst(root_node):
    if root_node is None:
        return
    postorder_traversal_bst(root_node.left_child)
    postorder_traversal_bst(root_node.right_child)       # Time Complexity is o(N)
    print(root_node.data)

#level order traversal order is level by level
def levelorder_traversal(root_node):
    if root_node is None:
        return
    custom_queue = LinkedListQueue()
    custom_queue.enqueue(root_node)
    while not custom_queue.is_empty():
        root = custom_queue.dequeue()
        print(root.data)
        if root.left_child:
            custom_queue.enqueue(root.left_child)

        if root.right_child:
            custom_queue.enqueue(root.right_child)      #Time complexity is o(N)

def search_node_bst(root_node, node_value):
    if root_node.data == node_value:
        print("Node Found")
    elif node_value <= root_node.data and root_node.left_child:
        if root_node.left_child.data == node_value:
            print("Node found")
        else:
            search_node_bst(root_node.left_child, node_value)
    elif node_value >= root_node.data and root_node.right_child:
        if root_node.right_child.data == node_value:
            print("Node found") 
        else:
           search_node_bst(root_node.right_child, node_value)       #Time complexity is o(logN)
    else:
        print("Node not found")

# Delete a node from BST :
#     Case 1 : Node to be deleted is a leaf node
#     Case 2 : Node to be deleted has one child
#     Case 3 : Node to be deleted has two children
def min_value(root_node): 
    # we need to find a successor for Case 3 before deleting the node with 2 children
    current = root_node
    while current.left_child is not None:
        current = current.left_child
    return current


def delete_node_bst(root_node, node_value):
    if root_node is None:
        return root_node
    if node_value< root_node.data:
        root_node.left_child = delete_node_bst(root_node.left_child, node_value)
    elif node_value > root_node.data:
        root_node.right_child = delete_node_bst(root_node.right_child, node_value)
    else:
        if root_node.left_child is None:
            temp = root_node.right_child
            root_node = None
            return temp
        if root_node.right_child is None:
            temp = root_node.left_child
            root_node = None
            return temp
        # two children find the successor . smallest node in the right sub tree
        temp = min_value(root_node.right_child)
        root_node.data = temp.data
        root_node.right_child = delete_node_bst(root_node.right_child, temp.data)
    return root_node


newBST = BSTNode(None)
insert_node(newBST, 70)
insert_node(newBST, 50)
insert_node(newBST, 90)
insert_node(newBST, 30)
insert_node(newBST, 60)
insert_node(newBST, 80)
insert_node(newBST, 100)
insert_node(newBST, 20)
insert_node(newBST, 40)
# preorder_traversal_bst(newBST)
# inorder_traversal_bst(newBST)
# postorder_traversal_bst(newBST)
# levelorder_traversal(newBST)
search_node_bst(newBST, 20)
delete_node_bst(newBST, 100)
levelorder_traversal(newBST)