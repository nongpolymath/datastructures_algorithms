from queues_lib.queue_linked_list import LinkedListQueue


LinkedListQueue

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


newBT = TreeNode("Drinks")

# Create children of Drinks
left_child = TreeNode("Hot")
right_child = TreeNode("Cold")

newBT.left_child = left_child
newBT.right_child = right_child

# Add children under Hot
tea = TreeNode("Tea") 
coffee = TreeNode("Coffee")
left_child.left_child = tea
left_child.right_child = coffee

# Add children under Cold
lemonade = TreeNode("Lemonade")
apple_juice = TreeNode("Apple Juice")
right_child.left_child = lemonade
right_child.right_child = apple_juice


print("--------Pre Order Traversal--------")
def pre_order_traversal(root_node):
    if not root_node:
        return
    print (root_node.value)
    pre_order_traversal(root_node.left_child)
    pre_order_traversal(root_node.right_child)

pre_order_traversal(newBT)

print("--------in Order Traversal--------")
def in_order_traversal(root_node):
    if not root_node:
        return
    if root_node.left_child:
        in_order_traversal(root_node.left_child)
    print (root_node.value)
    if root_node.right_child:
        in_order_traversal(root_node.right_child)

in_order_traversal(newBT)

print("--------post Order Traversal--------")
def post_order_traversal(root_node):
    if not root_node:
        return
    if root_node.left_child:
        post_order_traversal(root_node.left_child)
    if root_node.right_child:
        post_order_traversal(root_node.right_child)
    print(root_node.value)

post_order_traversal(newBT)

print("--------Level order Traversal--------")
def level_order_traversal(root_node):
    if not root_node:
        return
    else:
        new_queue = LinkedListQueue()
        new_queue.enqueue(root_node)
        while not (new_queue.is_empty()):
            current_node = new_queue.dequeue()
            print(current_node.value.value)
            if current_node.value.left_child:
                new_queue.enqueue(current_node.value.left_child)
            if current_node.value.right_child:
                new_queue.enqueue(current_node.value.right_child)

level_order_traversal(newBT)

def search_binary_tree(root_node, search_node_val):
    if not root_node:
        return None
    else:
        new_queue = LinkedListQueue()
        new_queue.enqueue(root_node)
        while new_queue.front is not None:
            current_node = new_queue.dequeue()
            if current_node.value.value == search_node_val:
                return current_node.value
            if current_node.value.left_child:
                new_queue.enqueue(current_node.value.left_child)
            if current_node.value.right_child:
                new_queue.enqueue(current_node.value.right_child)
        print(f"Search node value {search_node_val} not found:")
        return None
t_node = search_binary_tree(newBT, 'Lemonade')
print(t_node)

print("--------insert node--------")

def insert_node(root_node, node_value):
    new_node = TreeNode(node_value)
    if not root_node:
        root_node = new_node
        return root_node
    new_queue = LinkedListQueue()
    new_queue.enqueue(root_node)
    while not new_queue.is_empty():
        current = new_queue.dequeue()
        if current.value.left_child:
            new_queue.enqueue(current.value.left_child)
        else:
            current.value.left_child = new_node
            return new_node
        if current.value.right_child:
            new_queue.enqueue(current.value.right_child)
        else:
            current.value.right_child = new_node
            return new_node
    return None

print(insert_node(newBT, "Caramel Latte"))
level_order_traversal(newBT)

print("--------delete node--------")
# find deeepest node
# replace value with deepest node
# delete deepest node

def get_deepest_node(root_node):
    if not root_node:
        return
    new_queue = LinkedListQueue()
    new_queue.enqueue(root_node)
    while new_queue.front is not None:
        current_node = new_queue.dequeue()
        if current_node.value.left_child:
            new_queue.enqueue(current_node.value.left_child)
        if current_node.value.right_child:
            new_queue.enqueue(current_node.value.right_child)
    return current_node.value
d_node = get_deepest_node(newBT)
print(d_node)

def delete_deepest_node(root_node, d_node):
    if not root_node:
        return
    new_queue = LinkedListQueue()
    new_queue.enqueue(root_node)
    while new_queue.front is not None:
        current_node = new_queue.dequeue()
        if current_node.value == d_node:
            current_node.value = None
            return
        else:
            if current_node.value.left_child == d_node:
                current_node.value.left_child = None
                return
            else:
                new_queue.enqueue(current_node.value.left_child)
            if current_node.value.right_child == d_node:
                current_node.value.right_child = None
                return
            else:
                new_queue.enqueue(current_node.value.right_child)

def delete_node(root_node, value_to_delete):
    target_node = search_binary_tree(root_node, value_to_delete)
    
    if not target_node:
        print("Node not found")
        return
    
    deepest_node = get_deepest_node(root_node)
    target_node.value = deepest_node.value
    delete_deepest_node(root_node, deepest_node)
    return root_node

delete_node(newBT,"Lemonade")
level_order_traversal(newBT)

print("--------delete binary tree--------")

def delete_binary_tree(root_node):
    if root_node.left_child:
        root_node.left_child = None
    if root_node.right_child:
        root_node.right_child = None
    root_node = None 
# Note - Above delete_binary_tree method leaves out dangling sub-trees of the binary tree.Best way is to dereference recursively

def delete_entire_binary_tree(root_node):
    if not root_node:
        return None
    delete_entire_binary_tree(root_node.left_child)
    delete_entire_binary_tree(root_node.right_child)
    root_node.left_child = None
    root_node.right_child = None
    root_node.value = None
    return None