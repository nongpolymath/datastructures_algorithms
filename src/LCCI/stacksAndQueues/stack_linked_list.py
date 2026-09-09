"""
stack LIFO implementaton using a singly linked list in python

"""
class StackNode:
    def __init__(self , data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, item):
        node = StackNode(item)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is None:
            raise IndexError("stack is empty")
        item = self.top.data
        self.top = self.top.next
        return item

    def peek(self):
        if self.top is None:
            raise IndexError("stack is empty")
        return self.top.data

    def is_empty(self):
        return True if self.top is None else False


"""
Python's built-in list already is a dynamic array with O(1) amortized append/pop from the end, 
so the idiomatic, everyday Python stack is just:

stack = []
stack.append(10)   # push
stack.append(20)
stack.pop()         # pop -> 20
stack[-1]           # peek -> 10
len(stack) == 0     # is_empty

"""