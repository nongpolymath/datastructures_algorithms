class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    """
    LIFO stack using a singly linked list.
    """
    def __init__(self):
        """
        Initialize an empty Stack.
        """
        self.top = None
        self._size = 0
    
    @property   
    def is_empty(self):
        """
        Check if the stack is empty.
        """
        return self.top is None
    
    def push(self, value):
        """
        Push an element onto the stack.
        """
        new_node = Node(value)
        if self.is_empty:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self._size +=1
        
    def pop(self):
        """
        Remove and return the top element.
        """
        if self.is_empty:
            raise IndexError("cannot pop from an empty stack")
        popped_node = self.top
        self.top = self.top.next
        self._size -=1
        return popped_node.value

    def peek(self):
        """
        Return the top element without removing it.
        """
        if self.is_empty:
            raise IndexError("cannot peek on an empty stack")
        return self.top.value
    
    def size(self):
        """Return the number of elements.
        """
        return self._size
    
    def __iter__(self):
        """
        Iterate over the stack.
        """
        curr = self.top
        while curr:
            yield curr
            curr = curr.next
            
    # def __str__(self):
    #     """String representation of the stack."""
    #     node_values = [str(x.value) for x in self]
    #     return "\n".join(node_values)
    
    def __repr__(self):
        """Developer-friendly string representation."""
        stack_values = [x.value for x in self]
        return f"{self.__class__.__name__} ({stack_values !r})"

ss = Stack()
ss.push(1)
ss.push(2)
ss.push(3)
ss.push(4)
ss.push(5)
