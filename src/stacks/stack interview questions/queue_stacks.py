class Stack:
    def __init__(self):
        self.data = []
    
    def __iter__(self):
        for x in reversed(self.data):
            yield x
        
    
    def __repr__(self):
        return " -> ".join([str(x) for x in self])
    
    def push(self, value):
        self.data.append(value)
    
    def pop(self):
        if not self.data:
            return None
        return self.data.pop()

class QueueStacks:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()
        
    def enqueue(self,value):
        self.in_stack.push(value)
    
    def dequeue(self):
        if not self.in_stack:
            raise IndexError("Cannot pop from an empty Queue")
        if not self.out_stack:
            while self.in_stack:
                val = self.in_stack.pop()
                self.out_stack.push(val)
        if not self.out_stack:
            raise IndexError("Cannot dequeue from an empty queue")
        return self.out_stack.pop()
        