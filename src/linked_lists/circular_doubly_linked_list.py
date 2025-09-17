class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return self.value
    
    
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    # this constructor is for instantiating the class with a single node
    # def __init__(self, value):
    #     new_node = Node(value)
    #     new_node.next = new_node
    #     new_node.prev = new_node
    #     self.head = new_node
    #     self.tail = new_node
    #     self.length =1

    def __str__(self):
        current = self.head
        result = ""
        while current:
            result += str(current.value)
            current = current.next
            if current == self.head:
                break
            result += " <-> "
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.head.prev = new_node
            self.tail = new_node
        self.length +=1
        
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.tail.next = new_node
            new_node.prev = self.tail
            self.head = new_node
        self.length+=1

    def traverse(self):
        """
        Traverses the circular doubly linked list from head to tail.

        Starts from the head and iterates through each node in the list
        until it returns to the head, completing one full circle. This method
        is typically used to visit or print each node's value in sequence.
        If the list is empty, the method does nothing.
        """
        if self.node is None:
            return None
        current = self.head
        while current:
            print(current.value)
            current = current.next
            if current == self.head:
                break
            
    def reverse_traverse(self):
        """
        Traverses the circular doubly linked list in reverse order, from tail to head.

        Starts from the tail and iterates backward through each node in the list
        using the `prev` pointers until it returns to the tail, completing one
        full circle. This method is typically used to visit or print each node's
        value in reverse sequence. If the list is empty, the method does nothing.
        """
        if self.node is None:
            return None
        current = self.tail
        while current:
            print(current.value)
            current = current.prev
            if current == self.tail:
                break
            
    def search(self,value):
        if self.head is None:
            raise ValueError("Cannot search an empty list")
        current = self.head
        while True:
            if current.value == value:
                return current
            current = current.next
            if current == self.head:
                return None
            
    def get(self,index):
        """
        Return the node at position `index` (0‐based) in the circular doubly‐linked list.
        Raises IndexError if index is out of range [0, self.length).
        """
        if index<0 or index>=self.length:
            raise IndexError("Index exceeds bounds of the circular linked list")
        if index < self.length//2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length-1, index, -1):
                current = current.prev
        return current

    def set(self,value,index):
        """
        Set the .value of the node at `index` to `value`.
        Raises IndexError if index is invalid.
        """
        temp = self.get(index)
        temp.value = value
    
    def insert(self, index, value):
        """
        Insert a new node with the given value at the specified index in the circular
        doubly‑linked list
        """
        if index == 0:
            self.prepend(value)
            return
        elif index == self.length-1:
            self.append(value)
            return
        else:
            new_node = Node(value)
            temp = self.get(index)
            new_node.next = temp.next
            new_node.prev = temp
            temp.next.prev = new_node
            temp.next = new_node
            self.length += 1
            
    def pop_first(self):
        """
        Removes and returns the first node from the circular doubly linked list.

        """
        if self.head is None:
            raise ValueError("cannot pop on an empty list")
        elif self.length == 1:
            popped_node = self.head
            popped_node.next = None
            popped_node.prev = None
            self.head = self.tail = None
        else:
            popped_node = self.head
            self.head = self.head.next
            self.head.prev = popped_node.prev
            self.tail.next = self.head
            popped_node.next = None
            popped_node.prev = None
        self.length -= 1
        return popped_node

    def pop(self):
        if self.head is None :
            raise ValueError("cannot pop on an empty circular doubly linked list")
        elif self.length ==1:
            popped_node = self.head
            popped_node.next = None
            popped_node.prev= None
            self.tail=self.head= None
        else:
            popped_node = self.tail
            self.tail = self.tail.prev
            self.tail.next = popped_node.next
            popped_node.next.prev = self.tail
            popped_node.next = None
            popped_node.prev = None
        self.length -=1
        return popped_node

    def remove(self, index):
        if self.head is None:
            raise IndexError("Cannot remove from an empty circular doubly‑linked list")
        popped_node = self.get(index)
        if index == 0:
            self.pop_first()
            return
        elif index ==self.length-1:
            self.pop()
            return
        else:
              prev_node = popped_node.prev
              next_node = popped_node.next
              prev_node.next = next_node
              next_node.prev = prev_node
              popped_node.next = None
              popped_node.prev = None
              self.length -=1
              return popped_node

    def delete(self):
        """
        Remove all nodes from the circular doubly‑linked list.
        After calling, head and tail are None, length is 0,
        and all nodes become unreachable (eligible for GC).
        """
        if self.head is None:
            return
        self.tail = None
        self.head = None
        self.length = 0

cdll = CircularDoublyLinkedList()
cdll.append(10)
cdll.append(20)
cdll.append(30)
cdll.append(40)
cdll.append(50)
cdll.prepend(5)
print(cdll)
# print(cdll.pop_first().value)
# cdll.pop()
cdll.remove(2)
cdll.delete()
print(cdll)