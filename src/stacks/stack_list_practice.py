class StackList:
    """
    A LIFO (Last-In, First-Out) stack implementation using a Python list.
    The end of the list is treated as the top of the stack.
    """
    def __init__(self):
        """
        Initializes an empty StackList.
        """
        self.items = []
        
    def push(self, value):
        """
        Pushes an element onto the top of the stack.

        Args:
            value: The element to be added to the stack.
        """
        self.items.append(value)
        
    def pop(self):
        """
        Removes and returns the element from the top of the stack.

        Returns:
            Any: The element removed from the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.items.is_empty:
            raise IndexError("cannot pop on an empty LIFO stack")
        return self.items.pop()
    
    def peek(self):
        """
        Returns the element at the top of the stack without removing it.

        Returns:
            Any: The element at the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if not self.items:
            raise IndexError("cannot peek on an empty LIFO stack")
        return self.items[-1]
    
    @property
    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0
    
    @property
    def size(self):
        """
        Returns the number of elements in the stack.

        Returns:
            int: The number of elements in the stack.
        """
        return len(self.items)
    
    def __str__(self):
        """
        Returns a string representation of the stack top to bottom.

        Returns:
            str: A string representation of the stack.
        """
        return f"{self.__class__.__name__} {str(list(reversed(self.items)))}"
    
    
st = StackList()
st.push(1)
st.push(2)
st.push(3)
print(st)