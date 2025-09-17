from random import randint

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
class LinkedList:
    # A more pythonic way of representing the Node and Linked List class
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next
        
    def __str__(self):
        #use list comprehension instead of loop
        node_Values = [str(x.value) for x in self]
        return (" -> ").join(node_Values)

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length +=1
    
    def generate_nodes(self,min_value, max_value, length):
        for _ in range(length):
            self.append(randint(min_value,max_value))
            
    def get_kth_node_from_end(self, k_size):
        fast = self.head
        slow = self.head
        for _ in range(k_size):
            if fast is None:
                return None
            fast = fast.next
            
        while fast:
            fast = fast.next
            slow = slow.next
        return slow
    
    # code to partition a linked list around a value x , such that all nodes less than x come before all nodes greater than or equal to x
    def partition_around(self,x):
        # add dummy nodes
        if not self.head:
            return
        before_head = before_tail = Node(0) 
        after_head = after_tail = Node(0)
        
        # create reference pointer to head node
        current = self.head
        
        # while current is not None, if current.value<x append current to before list else append current to after list, keep moving the tail nodes 
        while current:
            if current.value < x:
                before_tail.next = current
                before_tail = before_tail.next
            else:
                after_tail.next = current
                after_tail = after_tail.next
            current = current.next
        # link the two nodes omitting the link dummy node
        before_tail.next = after_head.next
        #remove dangling logic , point tail node to None
        after_tail.next = None
        # point head to before_head of the stitched linked list
        self.head = before_head.next
        
def sum_linked_lists(ll1, ll2):
    """
    Sums two numbers represented by linked lists, where digits are stored in reverse order.

    Args:
        ll1 (LinkedList): The first linked list representing a number.
        ll2 (LinkedList): The second linked list representing a number.

    Returns:
        LinkedList: A new linked list representing the sum of the two input numbers.
    """

    # initialize pointers
    p1 = ll1.head
    p2 = ll2.head
    carry = 0
    dummy_node = Node(0)
    sum_ll = LinkedList()
    sum_ll.tail = dummy_node
    while p1 and p2 or carry:
        v1 = p1.value
        v2 = p2.value
        total = v1+v2+carry
        digit = total%10
        carry = total //10
        new_digit = Node(digit)
        sum_ll.tail.next = new_digit
        sum_ll.tail = sum_ll.tail.next
        sum_ll.length +=1
        p1 = p1.next
        p2 = p2.next
    sum_ll.head = dummy_node.next
    return sum_ll 

def intersection(ll1, ll2):
    """
    Finds the intersection node of two singly linked lists.

    An intersection is defined as the point where two linked lists merge and
    share the same subsequent nodes. This function assumes that if an
    intersection exists, the tails of both lists will be the same node.

    Args:
        ll1 (LinkedList): The first linked list.
        ll2 (LinkedList): The second linked list.

    Returns:
        Node or False: The intersection node if found, otherwise False.
    """
    
    if ll1.tail != ll2.tail:
        return False
    len1 = ll1.length
    len2 = ll2.length
    if len1 < len2:
        shorter_list, longer_list = ll1, ll2
    else:
        shorter_list, longer_list = ll2, ll1
    diff = abs(len1 - len2)
    shorter_node = shorter_list.head
    longer_node = longer_list.head 
    # traverse longer node till same distance to intersection
    for _ in range(diff):
        longer = longer.next
    while shorter_node is not longer_node:
        shorter_node = shorter_node.next
        longer_node = longer_node.next
    return shorter_node
    

# customLL = LinkedList()
# customLL.generate_nodes(15,80,10)
# print(customLL)
# print(customLL.get_kth_node_from_end(4).value)
# added function calls for creating linked lists to find sum of numbers stored in reverse in linked lists
ll1 = LinkedList()
ll2 = LinkedList()
ll1.append(7)
ll1.append(1)
ll1.append(6)
print(ll1)
ll2 = LinkedList()
ll2.append(5)
ll2.append(9)
ll2.append(2)
print(ll2)
print(sum_linked_lists(ll1,ll2))
