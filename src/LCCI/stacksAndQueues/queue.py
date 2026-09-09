"""
Implementation of a queue with two pointers , 
since a queue needs independent access to both ends (enqueue at the rear, dequeue at the front)
"""

class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        node = QueueNode(item)
        if self.rear is not None:
            self.rear.next = node
        self.rear = node
        if self.front is None:
            self.front = node

    def dequeue(self):
        if self.front is None:
            raise IndexError("dequeue from an empty queue")
        item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return item

    def peek(self):
        if self.front is None:
            raise IndexError("peek from an empty queue")
        return self.front.data

    def is_empty(self):
        return self.front is None