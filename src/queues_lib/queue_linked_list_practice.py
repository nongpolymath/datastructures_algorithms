class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def __str__(self):
        return f"{self.__class__.__name__} {self.value}"    

class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
    
    @property
    def is_empty(self):
        return self.rear == None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.length +=1
        
    def dequeue(self):
        if self.is_empty:
            return Exception("Queue is empty")
        popped_node = self.front
        self.front = self.front.next
        self.length -=1
        return popped_node.value
    
    def peek(self):
        if not self.is_empty:
            return self.front.value
        else:
            raise Exception("Empty Queue")
    
    def __iter__(self):
        current = self.front
        while current:
            yield current
            current = current.next
            
    def __repr__(self):
        queue_vals = " -> ".join([str(x.value) for x in self])
        return f"{self.__class__.__name__} {queue_vals}"
    
    
qll = QueueLinkedList()
qll.enqueue(1)
qll.enqueue(2)
qll.enqueue(3)
qll.enqueue(4)
qll.enqueue(5)
qll.peek()
qll.dequeue()
print(qll)