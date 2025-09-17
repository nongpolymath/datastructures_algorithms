class Node:
    """
    A node in a doubly linked list.

    Attributes:
        value: The data stored in the node.
        next: Reference to the next node in the list.
        prev: Reference to the previous node in the list.
    """
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    """
    A class representing a doubly linked list data structure.

    Attributes:
        head (Node): The first node in the linked list.
        tail (Node): The last node in the linked list.
        length (int): The number of nodes in the linked list.

    Methods:
        __init__(): Initializes an empty doubly linked list.
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def __str__(self):
        """
        Return a string representation of the doubly linked list.

        Returns:
            str: A string showing the elements of the list in order.
        """
        temp = self.head
        result = ""
        while temp:
            result += str(temp.value) + " <—> "
            temp = temp.next
        return result[0:-5]
    
    def append(self,value):
        """
        Appends a new node with the given value to the end of the doubly linked list.

        Parameters:
            value: The data to be stored in the new node.

        Side Effects:
            Modifies the list by adding a new node at the end.
            Updates the head and tail pointers as necessary.
            Increments the length of the list.
        """
        node = Node(value)
        if self.head == None:
            self.head = node
            self.tail= node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length +=1
        
    def prepend(self, value):
        """
        Inserts a new node with the specified value at the beginning of the doubly linked list.

        Args:
            value: The value to be stored in the new node.

        Raises:
            Any exceptions raised by the node creation or memory allocation.

        Returns:
            None
        """
        node = Node(value)
        if self.head ==None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.length +=1
        
    def traverse(self):
        """
        Traverse the doubly linked list and perform an action on each node.

        Yields:
            The data stored in each node as the list is traversed from head to tail.
        """
        current = self.head
        while current:
            print(current.value)
            current = current.next
            
    def reverse_traverse(self):
        """
        Traverse the doubly linked list in reverse order, starting from the tail and moving towards the head.

        Yields:
            The data stored in each node, from tail to head.
        """
        current = self.tail
        while current:
            print(current.value)
            current = current.prev
            
    def search(self, target):
        """
        Searches for the first occurrence of a node with the specified target value in the doubly linked list.

        Args:
            target: The value to search for in the list.

        Returns:
            int: The index of the first node containing the target value, or -1 if the value is not found.
        """
        current = self.head
        index = 0
        while current:
            if current.value == target:
                return index
            else:
                current = current.next
                index+=1
        return -1
    
    def get(self,index):
        """
        Retrieve the node at the specified index in the doubly linked list.

        Args:
            index (int): The position of the node to retrieve (0-based).

        Returns:
            Node: The node at the specified index if it exists, otherwise None.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if self.length <= index <0:
            raise IndexError("index out of bounds of linked list length")
        
        if index < self.length//2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length-1, index,-1):
                current = current.prev
        return current
    
    def set_value(self, value, index):
        """
        Sets the value of the node at the specified index in the doubly linked list.

        Parameters:
            value: The new value to assign to the node.
            index (int): The position of the node whose value is to be updated.

        Raises:
            IndexError: If the index is out of the bounds of the list.
        """
        if index >= self.length or index < 0:
            raise IndexError("index out of linked list range")
        node = self.get(index)
        node.value = value
    
    def insert(self, value, index):
        """
        Inserts a new node with the specified value at the given index in the doubly linked list.

        Args:
            value: The data to be stored in the new node.
            index (int): The position at which to insert the new node. Indexing starts at 0.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if index >= self.length or index < 0:
             raise IndexError("index out of linked list range")
        temp_node = self.get(index-1)
        if index == 0:
            self.prepend(value)
            return
        elif index == self.length:
            self.append(value)
            return
        else:
            new_node = Node(value)
            new_node.next = temp_node.next
            new_node.prev = temp_node
            temp_node.next.prev = new_node
            temp_node.next = new_node
        self.length +=1
        
    def pop_first(self):
        """
        Removes and returns the first node from the doubly linked list.

        Returns:
            Node or None: The removed node if the list is not empty; otherwise, None.

        Side Effects:
            Updates the head of the list. If the list becomes empty, also updates the tail.
        """
        if self.head is None:
            return None
        elif self.length ==1:
            self.head = None
            self.length -=1
        else:
            popped_node = self.head
            self.head = self.head.next
            self.head.prev = None
            popped_node.next = None
            self.length -=1
            return popped_node
            
    def pop(self):
        """
        Removes and returns the last node from the doubly linked list.

        Returns:
            The value of the removed node if the list is not empty; otherwise, None.
        """
        if self.head is None:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -=1
            return None
        else:
            popped_node = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            popped_node.prev = None
            self.length -=1
            return popped_node
            
    def remove(self, index):
        """
        Removes the node at the specified index from the doubly linked list.

        Args:
            index (int): The index of the node to remove (0-based).

        Returns:
            Node: The removed node.

        Raises:
            IndexError: If the index is out of bounds.
            ValueError: If the list is empty.
        """
        if self.head is None:
            raise ValueError("Linked List is empty")
        elif index <0 or index>= self.length:
            raise IndexError("Index exceeded linked list")
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        popped_node = self.get(index)
        prev_node = popped_node.prev
        prev_node.next = popped_node.next
        popped_node.next.prev = prev_node
        self.length -=1
        

dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.prepend(5)
dll.append(40)
dll.append(50)
print(dll)
print(dll.search(30))
print(dll.get(4).value)
dll.set_value(25,2)
print(dll)
dll.insert(100,5)
print(dll)
dll.remove(0)
print(dll)
