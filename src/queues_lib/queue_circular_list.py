class CircularQueue:
    """
    A fixed-size queue using a circular Python list.

    Attributes:
        _data (list): The internal list used to store queue elements.
        _capacity (int): The maximum capacity of the queue.
        _front (int): Index of the front element.
        _rear (int): Index of the rear element.
        _size (int): Current number of elements in the queue.
    """
    def __init__(self, capacity):
        """
        Initializes an empty circular queue with a given capacity.
        """
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Capacity must be a positive integer.")
        self._data = [None] * capacity
        self._capacity = capacity
        self._front = 0
        self._rear = -1  # Indicates an empty queue
        self._size = 0

    def is_empty(self):
        """
        Returns True if the queue is empty, False otherwise.
        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return self._size == 0

    def is_full(self):
        """
        Returns True if the queue is full, False otherwise.
        Returns:
            bool: True if the queue is full, False otherwise.
        """
        return self._size == self._capacity

    def enqueue(self, x):
        """
        Adds an element to the rear.
        Raises:
            Exception: If the queue is full.
        """
        if self.is_full():
            raise Exception("Queue is full. Cannot enqueue.")
        
        self._rear = (self._rear + 1) % self._capacity
        self._data[self._rear] = x
        self._size += 1

    def dequeue(self):
        """
        Removes and returns the element from the front.
        Raises:
            Exception: If the queue is empty.
        """
        if self.is_empty():
            raise Exception("Queue is empty. Cannot dequeue.")
        
        item = self._data[self._front]
        self._data[self._front] = None  # Optional: clear the reference
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return item

    def peek(self):
        """
        Returns the front element without removing it.
        Raises:
            Exception: If the queue is empty.
        """
        if self.is_empty():
            raise Exception("Queue is empty. Cannot peek.")
        return self._data[self._front]

    def size(self):
        """
        Returns the number of elements in the queue.
        Returns:
            int: The number of elements in the queue.
        """
        return self._size

    def __str__(self):
        """
        Returns a string representation.
        """
        if self.is_empty():
            return "Queue: []"
        
        elements = []
        for i in range(self._size):
            index = (self._front + i) % self._capacity
            elements.append(str(self._data[index]))
        return "Queue: [" + ", ".join(elements) + "]"