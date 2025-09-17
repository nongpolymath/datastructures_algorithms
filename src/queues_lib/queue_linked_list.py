class Node:
    """A node in a linked list."""
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListQueue:
    """
    A Queue implementation using a singly linked list.

    Attributes:
        front (Node): The front (head) of the queue.
        rear (Node): The rear (tail) of the queue.
    """
    def __init__(self):
        self.front = None  # Head of the queue
        self.rear = None   # Tail of the queue

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:
            # Queue is empty
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Queue is empty. Cannot dequeue.")
            return None
        removed_value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None  # Queue became empty
        return removed_value

    def is_empty(self):
        return self.front is None

    def peek(self):
        if self.front:
            return self.front.value
        return None

    def display(self):
        current = self.front
        elements = []
        while current:
            elements.append(current.value)
            current = current.next
        print("Queue:", elements)
