class Node:
    def __init__(self, value=None, next = None):
        self.value = value
        self.next = next
        
class MinStackLinkedList:
    def __init__(self):
        self.main_top = None
        self.min_top = None
        
    def push(self, value):
        # Create a new node and point its 'next' to the current top
        new_main = Node(value, self.main_top)
        # The new node is now the top of the main stack
        self.main_top = new_main

        # If the min_stack is empty or the new value is a new minimum,
        # push it to the min_stack.
        if self.min_top is None or value <= self.min_top.value:
            new_min = Node(value, self.min_top)
            self.min_top = new_min

    def pop(self):
        # Check if the stack is empty before popping
        if self.main_top is None:
            raise IndexError("pop from an empty stack")

        popped_node = self.main_top
        self.main_top = self.main_top.next

        # If the popped value is the current minimum, pop from the min_stack too
        if popped_node.value == self.min_top.value:
            self.min_top = self.min_top.next
        return popped_node.value

    def get_min(self):
        if self.min_top is None:
            raise ValueError("Stack is empty, no minimum")
        return self.min_top.value