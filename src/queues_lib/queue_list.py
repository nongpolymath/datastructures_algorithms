class Queue:
    """
    A Queue implementation using a Python list.

    This implementation uses `insert(0, x)` for enqueue operations
    and `pop()` for dequeue operations to achieve O(1) complexity
    for dequeue. However, `insert(0, x)` has O(n) complexity.

    Attributes:
        _data (list): The internal list used to store queue elements.
    """
    def __init__(self):
        """
        Initializes an empty Queue.
        """
        self._data = []

    def enqueue(self, x):
        """
        Adds an element to the rear of the queue.

        Args:
            x: The element to be added to the queue.
        """
        # Add at the front of the list so that popping from the end is O(1)
        self._data.insert(0, x)  

    def dequeue(self):
        """
        Removes and returns the element from the front of the queue.

        Returns:
            Any: The element removed from the front of the queue.
        """
        return self._data.pop()    # O(1) complexity for popping from the end
