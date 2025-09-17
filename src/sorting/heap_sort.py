from binary_heap import heapify_tree_insert

def heapify(custom_list, n , i):
    smallest = i
    l = 2*i +1
    r = 2*i +2
    