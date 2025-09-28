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
        return
    else:
        new_queue = LinkedListQueue()
        new_queue.enqueue(root_node)
        while new_queue.front is not None:
            current_node = new_queue.dequeue()
            if current_node.value.value == search_node_val:
                return True
            if current_node.value.left_child:
                new_queue.enqueue(current_node.value.left_child)
            if current_node.value.right_child:
                new_queue.enqueue(current_node.value.right_child)
        print(f"Search node value {search_node_val} not found:")
        return False

print(search_binary_tree(newBT, 'Lemonade'))

print("--------insert node--------")