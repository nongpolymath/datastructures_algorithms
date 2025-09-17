class StackListLimited:
    def __init__(self, max_size):
        self.max_size = max_size
        self.items = []
        
    @property
    def length(self):
        return len(self.items)
    
    @property
    def is_empty(self):
        return self.length == 0
    
    @property
    def is_full(self):
        return self.length >= self.max_size
    
    def push(self, value):
        if self.length >= self.max_size:
            raise OverflowError("Stack is full")
        self.items.append(value)
        
    def pop(self):
        if self.is_empty:
            raise IndexError("cannot pop from an empty Stack list")
        self.items.pop()
        
    def peek(self):
        if self.is_empty:
            raise IndexError("cannot pop from an empty Stack list")
        return self.items[-1]
        
    def __str__(self):
        """String representation of the stack."""
        return f"Stack(top→bottom): {list(reversed(self.items))}"