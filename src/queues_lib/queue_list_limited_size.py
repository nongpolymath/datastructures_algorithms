class LimitedQueue:
    """
    A Queue implementation using a Python list with a fixed capacity.

    This implementation uses a standard Python list. Enqueue operations
    append to the end of the list, and dequeue operations remove from the
    beginning of the list.

    Attributes:
        queue (list): The internal list used to store queue elements.
        capacity (int): The maximum number of elements the queue can hold.
    """
    def __init__(self, capacity):
        """
        Initializes an empty LimitedQueue with a given capacity.

        Args:
            capacity (int): The maximum number of elements the queue can hold.
        """
        # Validate capacity to ensure it's a positive integer
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Capacity must be a positive integer.")
        self.queue = []
        self.capacity = capacity

    def enqueue(self, value):
        """
        Adds an element to the rear of the queue.

        Args:
            value: The element to be added to the queue.

        Returns:
            bool: True if the element was successfully enqueued, False otherwise.
        """
        if len(self.queue) >= self.capacity:
            print("Queue is full. Cannot enqueue.")
            return False
        self.queue.append(value)
        return True

    def dequeue(self):
        """
        Removes and returns the element from the front of the queue.

        Returns:
            Any: The element removed from the front of the queue, or None if the queue is empty.

        Note:
            This operation has O(N) time complexity because `pop(0)`
            requires shifting all subsequent elements.
        """
        if not self.queue:
            print("Queue is empty. Cannot dequeue.")
            return None
        return self.queue.pop(0)  # O(N) time due to shifting

    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self.queue) == 0

    def is_full(self):
        """
        Checks if the queue is full.

        Returns:
            bool: True if the queue is full, False otherwise.
        """
        return len(self.queue) == self.capacity

    def peek(self):
        """
        Returns the element at the front of the queue without removing it.

        Returns:
            Any: The element at the front of the queue, or None if the queue is empty.
        """
        if self.queue:
            return self.queue[0]
        return None

    def __str__(self):
        """
        Returns a string representation of the queue.
        """
        return str(self.queue)
