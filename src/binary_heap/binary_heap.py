class Heap:
    def __init__(self, size):
        self.custom_list = (size + 1) * [None]
        self.heap_size = 0
        self.max_size = size

def peek_of_heap(root_node):
    if root_node:
        root_node.custom_list[1]
    else:
        return None
    
def size_of_heap(root_node):
    if not root_node:        
        return None
    else:
        return root_node.heap_size

def level_order_traversal(root_node):
    if not root_node:
        return
    for i in range(1, root_node.heap_size + 1):
        print(root_node.custom_list[i])


def heapify_tree_insert(root_node, index , heap_type):
    # Time Space complexity = o(logN)
    parent_index = index //2
    if index <= 1:
        return
    if heap_type == 'Min':
        if root_node.custom_list [index] < root_node.custom_list[parent_index]:
            temp = root_node.custom_list[index]
            root_node.custom_list[index] = root_node.custom_list[parent_index]
            root_node.custom_list[parent_index] = temp
            heapify_tree_insert(root_node, parent_index, heap_type) #Only recurses when a swap occurred
    elif heap_type == 'Max':
        if root_node.custom_list[index] > root_node.custom_list[parent_index]:
            temp = root_node.custom_list[index]
            root_node.custom_list[index] = root_node.custom_list[parent_index]
            root_node.custom_list[parent_index] = temp
            heapify_tree_insert(root_node, parent_index, heap_type)
        # Recursion is needed because a single swap may not be enough to satisfy heap condition— 
        # the inserted element might have to bubble all the way up to the root.

def insert_node(root_node, node_value, heap_type):
    if root_node.heap_size + 1 == root_node.max_size:
        return "The Heap is full"
    root_node.custom_list[root_node.heap_size + 1] = node_value
    root_node.heap_size += 1
    heapify_tree_insert(root_node, root_node.heap_size, heap_type) # o(log N ) complexity
    return "The node has been successfully inserted"

def heapify_tree_extract(root_node, index, heap_type):
    """
    Sift-down (heapify) the element at `index` in the heap (1-based indexing).
    Mutates root_node.custom_list and assumes root_node.heap_size is current.
    heap_type is 'Min' or 'Max'.
    """
    left = 2 * index
    right = 2 * index + 1

    # No children
    if root_node.heap_size < left:
        return

    # Only left child exists
    if root_node.heap_size == left:
        if heap_type == 'Min':
            if root_node.custom_list[index] > root_node.custom_list[left]:
                root_node.custom_list[index], root_node.custom_list[left] = \
                    root_node.custom_list[left], root_node.custom_list[index]
        else:  # Max
            if root_node.custom_list[index] < root_node.custom_list[left]:
                root_node.custom_list[index], root_node.custom_list[left] = \
                    root_node.custom_list[left], root_node.custom_list[index]
        return

    # Both children exist
    if heap_type == 'Min':
        # choose the smaller child
        swap_child = left if root_node.custom_list[left] < root_node.custom_list[right] else right
        if root_node.custom_list[index] > root_node.custom_list[swap_child]:
            root_node.custom_list[index], root_node.custom_list[swap_child] = \
                root_node.custom_list[swap_child], root_node.custom_list[index]
            heapify_tree_extract(root_node, swap_child, heap_type)  # <-- recursion needed
    else:  # Max
        # choose the larger child
        swap_child = left if root_node.custom_list[left] > root_node.custom_list[right] else right
        if root_node.custom_list[index] < root_node.custom_list[swap_child]:
            root_node.custom_list[index], root_node.custom_list[swap_child] = \
                root_node.custom_list[swap_child], root_node.custom_list[index]
            heapify_tree_extract(root_node, swap_child, heap_type)


def extract_node(root_node, heap_type):
    if root_node.heap_size == 0:
        return "The Heap is empty"
    extracted_node = root_node.custom_list[1]
    root_node.custom_list[1] = root_node.custom_list[root_node.heap_size]
    root_node.custom_list[root_node.heap_size] = None
    root_node.heap_size -= 1
    heapify_tree_extract(root_node, 1, heap_type) # o(log N) complexity
    return extracted_node

def delete_bin_heap(root_node):
    root_node.custom_list = None    # o(1) complexity

new_heap = Heap(5)
insert_node(new_heap, 4, "Max")
insert_node(new_heap, 5, "Max")
insert_node(new_heap, 2, "Max")
insert_node(new_heap, 1, "Max")
extract_node(new_heap, "Max")
level_order_traversal(new_heap)