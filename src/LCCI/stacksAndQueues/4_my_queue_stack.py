"""
Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.
core idea - Two-stack design
in : new elements get pushed here. O(1).
out : elements get popped/peeked from here (front of the queue).

Rule: only transfer in -> out when out is empty. If out already has elements, its top is already correct.
"""

class MyQueue(object):

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self):
        self.in_stack.append()

    def pop(self):
        self._transfer_stack()
        return self.out_stack.pop()

    def peek(self):
        self._transfer_stack()
        return self.out_stack[-1]

    def empty(self):
        return not self.in_stack and not self.out_stack

    def _transfer_stack(self):
        if not self.out_stack:
            while self.in_stack:
                val = self.in_stack.pop()
                self.out_stack.append(val)