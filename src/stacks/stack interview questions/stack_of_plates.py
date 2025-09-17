class SetOfStacks:
    def __init__(self, capacity):
        if capacity < 1:
            raise ValueError("Capacity must be >= 1")
        self.capacity = capacity
        self.stacks = []
        
    def push(self, value):
        if not self.stacks or len(self.stacks[-1]) == self.capacity:
            self.stacks.append([value])
        else:
            self.stacks[-1].append(value)
        
    def pop(self):
        if not self.stacks:
            raise IndexError("Cannot pop on an empty stack")
        val = self.stacks[-1].pop()
        if len(self.stacks[-1])==0:
            self.stacks.pop()
        return val
    
    def pop_at_index(self, index):
        if index< 0 or index>=len(self.stacks):
            raise IndexError("Index exceeds bounds of stack")
        if not self.stacks[index]:
            raise IndexError("cannot pop from empty sub-stack")
        val = self.stacks[index].pop()
        if len(self.stacks[index]) == 0:
            self.stacks.pop(index)
        return val