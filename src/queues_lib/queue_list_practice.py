class QueueList:
    """
    A FIFO (First-In, First-Out) queue implementation using a Python list.
    Dequeueing is O(n) due to `pop(0)`.
    """
    def __init__(self):
        """Initializes an empty queue."""
        self.items = []

    def __str__(self):
        """Returns a string representation of the queue."""
        return f"Queue: {self.items}"

    @property
    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return not self.items

    @property
    def size(self):
        """
        Returns the number of elements in the queue.

        Returns:
            int: The number of elements in the queue.
        """
        return len(self.items)

    def enqueue(self, value):
        """
        Adds an element to the rear of the queue (end of the list).

        Args:
            value: The element to be added.
        """
        self.items.append(value)

    def dequeue(self):
        """
        Removes and returns the element from the front of the queue.

        This is an O(n) operation.

        Returns:
            The element from the front of the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty:
            raise IndexError("Cannot dequeue from an empty queue.")
        return self.items.pop(0)

    def peek(self):
        """
        Returns the element at the front of the queue without removing it.

        Returns:
            The element at the front of the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty:
            raise IndexError("Cannot peek into an empty queue.")
        return self.items[0]


class QueueListLimited:
    """
    A FIFO queue implementation using a Python list with a maximum size.
    Dequeueing is O(n).
    """
    def __init__(self, max_size):
        """
        Initializes a limited-size queue.

        Args:
            max_size (int): The maximum number of items the queue can hold.
        """
        if not isinstance(max_size, int) or max_size <= 0:
            raise ValueError("max_size must be a positive integer.")
        self.max_size = max_size
        self.items = []

    def __str__(self):
        """Returns a string representation of the queue."""
        return f"Queue: {self.items} (Size: {self.size}/{self.max_size})"

    @property
    def size(self):
        """Returns the current number of items in the queue."""
        return len(self.items)

    @property
    def is_empty(self):
        """Checks if the queue is empty."""
        return self.size == 0

    @property
    def is_full(self):
        """Checks if the queue is full."""
        return self.size == self.max_size

    def enqueue(self, value):
        """
        Adds an element to the rear of the queue if it's not full.

        Args:
            value: The element to be added.

        Raises:
            OverflowError: If the queue is full.
        """
        if self.is_full:
            raise OverflowError("Cannot enqueue on a full queue.")
        self.items.append(value)

    def dequeue(self):
        """
        Removes and returns the element from the front of the queue.

        This is an O(n) operation.

        Returns:
            The element from the front of the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty:
            raise IndexError("Cannot dequeue from an empty queue.")
        return self.items.pop(0)

    def peek(self):
        """
        Returns the element at the front of the queue without removing it.

        Returns:
            The element at the front of the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty:
            raise IndexError("Cannot peek into an empty queue.")
        return self.items[0]