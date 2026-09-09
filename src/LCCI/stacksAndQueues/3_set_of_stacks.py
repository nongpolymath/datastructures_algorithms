"""
Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity. 
SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack (that is, pop ( ) should return the same values as it would if there were just a single stack).
"""

class StackOfPlates:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = [] # list of stack

    def push(self, val):
        if not self.stacks or len(self.stacks[-1]) >= self.capacity:
            self.stacks.append([])
        self.stacks[-1].append(val)

    def pop(self):
        if not self.stacks:
            return -1
        val = self.stacks[-1].pop()
        if not self.stacks[-1]:
            self.stacks.poop()
        return val

    def pop_at(self, index):
        if (not 0 <= index < len(self.stacks)) or not self.stacks[index]:
            return -1
        val = self.stacks[index].pop()
        if not self.stacks[index]:
            self.stacks.pop(index)
        return val