from queues_lib.queue_linked_list import LinkedListQueue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

newBT = TreeNode("Drinks")

left_child = TreeNode("Hot")
right_child = TreeNode("Cold")
tea = TreeNode("Tea") 
coffee = TreeNode("Coffee")
left_child.left_child = tea
left_child.right_child = coffee
newBT.right_child = right_child
newBT.left_child = left_child

#PreOrder Traversal - Root Node -> Left subtree -> Right Subtree

def pre_order_traversal(root_node):
    if not root_node:
        return
    print (root_node.data)
    pre_order_traversal(root_node.left_child)
    pre_order_traversal(root_node.right_child)
    
pre_order_traversal(newBT)

#Inorder Traversal - Left Subtree -> Root Node -> Right Subtree
print("------------------------------------\n")
def in_order_traversal(root_node):
    if not root_node:
        return
    in_order_traversal(root_node.left_child)
    print(root_node.data)
    in_order_traversal(root_node.right_child)
    
in_order_traversal(newBT)

#PostOrder Traversal - Left Subtree -> Right Subtree -> Root Node
print("------------------------------------\n")

def post_order_traversal(root_node):
    if not root_node:
        return
    post_order_traversal(root_node.left_child)
    post_order_traversal(root_node.right_child)
    print(root_node.data)
    
post_order_traversal(newBT)

print("------------------------------------\n")

def level_order_traversal(root_node):
    if not root_node:
        return
    else:
        custom_queue = LinkedListQueue()
        custom_queue.enqueue(root_node)
        while not(custom_queue.is_empty()):
            root = custom_queue.dequeue()
            print(root.data)
            if root.left_child is not None:
                custom_queue.enqueue(root.left_child)
                
            if root.right_child is not None:
                custom_queue.enqueue(root.right_child)
                
level_order_traversal(newBT)
print("------------------------------------\n")
def search_bt_level_order(root_node, node_value):
    if not root_node:
        return
    else:
        custom_queue = LinkedListQueue()
        custom_queue.enqueue(root_node)
        while not(custom_queue.is_empty()):
            root = custom_queue.dequeue()
            if root.data == node_value:
                return "Node Found"
            if root.left_child is not None:
                custom_queue.enqueue(root.left_child)
                
            if root.right_child is not None:
                custom_queue.enqueue(root.right_child)
        return "Not Found"
print(search_bt_level_order(newBT, "Tea"))

print("------------level order-insert-node---------------------\n")

def insert_node(rootnode, new_node):
    if not rootnode:
        rootnode = new_node
    else:
        custom_queue = LinkedListQueue()
        custom_queue.enqueue(rootnode)
        while not(custom_queue.is_empty()):
            root = custom_queue.dequeue()
            if root.left_child is not None:
                custom_queue.enqueue(root.left_child)
            else:
                root.left_child = new_node
                return "Succesfully inserted"
            if root.right_child is not None:
                custom_queue.enqueue(root.right_child)
            else:
                root.right_child = new_node
                return "Successfully inserted"

newnode = TreeNode("Cola")
print(insert_node(newBT, newnode))

print("------------level order-traversal-delete-node---------------------\n")
# Find the target node (the one we want to delete).
# Find the deepest rightmost node (last node in level order).
# Replace target node’s value with deepest node’s value.
# Delete the deepest node.

def get_deepest_node(root_node):
    if not root_node:
        return
    else:
        custom_queue = LinkedListQueue()
        custom_queue.enqueue(root_node)
        while not custom_queue.is_empty():
            root = custom_queue.dequeue()
            if root.left_child is not None:
                custom_queue.enqueue(root.left_child)
            if root.right_child is not None:
                custom_queue.enqueue(root.right_child)
                
        deepest_node = root.data
        print(f"deepest node is {deepest_node} \n")
        return root
    
def delete_deepest_node(root_node, deepest_node):
    if not root_node:
        return
    else:
        custom_queue = LinkedListQueue()
        custom_queue.enqueue(root_node)
        while not custom_queue.is_empty():
            root = custom_queue.dequeue()
            if root.data == deepest_node.data:
                root = None
                return
            if root.left_child is not None:
                if root.left_child.data == deepest_node.data:
                    root.left_child = None
                    return
                custom_queue.enqueue(root.left_child)
            if root.right_child is not None:
                if root.right_child.data == deepest_node.data:
                    root.right_child = None
                    return
                custom_queue.enqueue(root.right_child)
                

def delete_node_bt(root_node, node):
    if not root_node:
        return
    else:
        custom_queue = LinkedListQueue()
        custom_queue.enqueue(root_node)
        while not custom_queue.is_empty():
            root = custom_queue.dequeue()
            if root.data == node:
                deepest_node = get_deepest_node(root_node)
                root.data = deepest_node.data
                delete_deepest_node(root_node, deepest_node)
                return "deepest node deleted"
            if root.left_child is not None:
                custom_queue.enqueue(root.left_child)
                
            if root.right_child is not None:
                custom_queue.enqueue(root.right_child)
        return "Not Found"
        
        
def delete_bt(root_node):
    root_node.left_child = None
    root_node.right_child = None
    root_node.data = None

delete_node_bt(newBT, 'Tea')
level_order_traversal(newBT)
# d_node = get_deepest_node(newBT)
# delete_deepest_node(newBT,d_node)
# level_order_traversal(newBT)