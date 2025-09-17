class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next  = nxt

class Stack:
    def __init__(self):
        self.top = None   # Points to the top Node
        self._size = 0

    def is_empty(self):
        return self.top is None

    def push(self, item):
        # Create a new node whose next is the old top
        node = Node(item, self.top)
        self.top = node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        node = self.top
        self.top = node.next
        self._size -= 1
        return node.value

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.top.value

    def size(self):
        return self._size
    
    # def __iter__(self):
    #     curNode = self.top
    #     while curNode:
    #         yield curNode
    #         curNode = curNode.next

    # def __str__(self):
    #     values = [str(x.value) for x in self]
    #     return '\n'.join(values)
    
    def __repr__(self):
        # Show stack from top down
        items = []
        curr = self.top
        while curr:
            items.append(curr.value)
            curr = curr.next
        return f"Stack(top→bottom): {items}"


ss = Stack()
ss.push(25)
ss.push(30)
ss.push(35)
ss.push(40)
print(ss)