class QueueCircularList:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.items = [None] * self.max_capacity #fixed pre-allocated memory
        self.front = 0
        self.rear = 0
        self._size = 0

    @property
    def is_full(self):
        return self._size == self.max_capacity

    @property
    def is_empty(self):
        return self._size == 0

    def enqueue(self, value):
        if self.is_full:
            raise OverflowError("Queue is full")
        if self.is_empty:
            self.items[self.front]= value
        else:
            self.rear = (self.rear+1)%self.max_capacity
            self.items[self.rear] = value
        self._size +=1
        
    def dequeue(self):
        if self.is_empty:
            raise Exception("Queue is empty")
        dq_value = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front+1)%self.max_capacity
        self._size -=1
        return dq_value
    
    def peek(self):
        return self.items[self.front]
    
    def __str__(self):
        if self.is_empty:
            return "Queue: []"
        queue_list = [x for x in self]
        return f"{self.__class__.__name__ } in FIFO order: {queue_list}"
    
    def __iter__(self):
        """Yield items in FIFO order, from front to rear, wrapping around."""
        front = self.front
        for _ in range(front,self.rear+1):
            yield self.items[front]
            front = (front+1)% self.max_capacity
    
    
cq = QueueCircularList(max_capacity=5)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.enqueue(5)
print(cq.dequeue())
print(cq.peek())
print(cq)