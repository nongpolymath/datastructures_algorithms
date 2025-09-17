from queues_lib.queue_linked_list import LinkedListQueue

class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.height = 1

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
    if not root_node:
        return
    custom_queue = LinkedListQueue()
    custom_queue.enqueue(root_node)
    while not custom_queue.is_empty():
        node = custom_queue.dequeue()
        print(node.data)
        if node.left_child is not None:
            custom_queue.enqueue(node.left_child)

        if node.right_child is not None:
            custom_queue.enqueue(node.right_child)      #Time complexity is o(N)

# Left-Left condition 
# Left-Right condition
# Right Right condition
# Right-Left condition
def get_height(root_node):
    if not root_node:
        return 0
    return root_node.height

def right_rotate(disbalanced_node):
    new_root = disbalanced_node.left_child
    disbalanced_node.left_child = disbalanced_node.left_child.right_child
    new_root.right_child = disbalanced_node
    disbalanced_node.height =1+ max(get_height(disbalanced_node.left_child), get_height(disbalanced_node.right_child))
    new_root.height =1+ max(get_height(new_root.left_child), get_height(new_root.right_child))
    return new_root

def left_rotate(disbalanced_node):
    new_root = disbalanced_node.right_child
    disbalanced_node.right_child = disbalanced_node.right_child.left_child
    new_root.left_child = disbalanced_node
    disbalanced_node.height =1+ max(get_height(disbalanced_node.left_child), get_height(disbalanced_node.right_child))
    new_root.height =1+ max(get_height(new_root.left_child), get_height(new_root.right_child))
    return new_root

def get_balance(root_node):
    if not root_node:
        return
    return get_height(root_node.left_child) - get_height(root_node.right_child)

def insert_node_avl(root_node, node_value):
    if not root_node:
        root_node = AVLNode(node_value)
        return root_node
    if node_value < root_node.data:
        root_node.left_child = insert_node_avl(root_node.left_child, node_value)
    elif node_value > root_node.data:
        root_node.right_child = insert_node_avl(root_node.right_child, node_value)
    else:
        return root_node
    
    root_node.height = 1 + max(get_height(root_node.left_child), get_height(root_node.right_child))
    balance = get_balance(root_node)
    if balance > 1 and node_value < root_node.left_child.data: # left left condition
        return right_rotate(root_node)
    if balance > 1 and node_value > root_node.left_child.data: # left right condition
        root_node.leftChild = left_rotate(root_node.left_child)
        return right_rotate(root_node)
    if balance < -1 and node_value > root_node.right_child.data: # right right condition
        return left_rotate(root_node)
    if balance < -1 and node_value < root_node.right_child.data: # right left condition
        root_node.right_child = right_rotate(root_node.right_child)
        return left_rotate(root_node)
    return root_node

def get_min_value_node(root_node):
    if root_node is None or root_node.left_child is None:
        return root_node
    return get_min_value_node(root_node)

def delete_node(root_node, node_value):
    if root_node is None:
        return root_node
    if node_value < root_node.data:
        root_node.left_child = delete_node(root_node.left_child, node_value)
    elif node_value > root_node.data:
        root_node.right_child = delete_node(root_node.right_child, node_value)
    else:
        if root_node.left_child is None:
            temp = root_node.right_child 
            root_node = None
            return temp
        elif root_node.right_child is None:
            temp = root_node.left_child 
            root_node = None
            return temp
        temp = get_min_value_node(root_node.right_child) 
        root_node.data = temp.data
        root_node.right_child = delete_node(root_node.right_child, temp.data)
        
    balance = get_balance(root_node)
    if balance > 1 and get_balance(root_node.left_child) >=0: # Left-Left Condition
        return right_rotate(root_node)
    if balance > 1 and get_balance(root_node.left_child) < 0: # Left-Right Condition
        root_node.left_child = left_rotate(root_node.left_child)
        return right_rotate(root_node)
    if balance < -1 and get_balance(root_node.right_child) <= 0: # Right-Right Condition
        return left_rotate(root_node)
    if balance < -1 and get_balance(root_node.right_child) > 0: # Right-Left Condition
        root_node.right_child = right_rotate(root_node.right_child)
        return left_rotate(root_node)
    return root_node

def delete_avl_tree(root_node):
    root_node.data = None
    root_node.left_child = None
    root_node.right_child = None
    return "The AVL tree has been successfully deleted"

new_avl = AVLNode(5)
new_avl = insert_node_avl(new_avl, 10)
new_avl = insert_node_avl(new_avl, 15)
new_avl = insert_node_avl(new_avl, 20)
levelorder_traversal(new_avl)