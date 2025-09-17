class Node:
    """Node class for a singly linked list.
    
    Attributes:
        data: The data stored in the node.
        next: Pointer to the next node in the linked list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """Singly linked list class.
    
    Attributes:
        head: Pointer to the first node in the linked list.
        tail: Pointer to the last node in the linked list.
        length: The number of nodes in the linked list.
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        """traverse through an entire linked list and return a string representation of the list
        Returns:
            _type_: string representation of the linked list
        """
        temp_node = self.head
        result = ""
        if temp_node is None:
            return "Empty list"    
        while temp_node is not None:
            result += str(temp_node.data) + " -> "
            temp_node = temp_node.next

        return result[:-4]  # Remove the last " -> " for a cleaner output

    def prepend(self, data):
        """Prepend a new node with the given data to the linked list.
        
        Args:
            data: The data to be added to the new node.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def append(self, data):
        """Append a new node with the given data to the linked list.
        
        Args:
            data: The data to be added to the new node.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
        
    def insert(self, index, data):
        """Insert a new node with the given data at the specified index in the linked list.
        
        Args:
            index: The position where the new node should be inserted.
            data: The data to be added to the new node.
        """
        new_node = Node(data)
        
        if index ==0 and index> self.length:
            new_node.next = self.head
            self.head = new_node
        elif self.length==0 and index==0:
            self.head = new_node
            self.tail = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
            if new_node.next is None:  # If inserted at the end, update tail
                self.tail = new_node
        self.length +=1
        
    def traverse(self):
        """Traverse the linked list and return a list of node data."""
        current = self.head
        while current is not None:
           print(current.data)
           current = current.next
           
    def search(self,value):
        """Search for a node with the given value in the linked list.
        
        Args:
            value: The value to search for in the linked list.
        
        Returns:
            Node: The node containing the value, or None if not found.
        """
        current = self.head
        index = 0
        while current:
            if current.data == value:
                print(f"Node found with value:{current.data} at index {index}")   
                return current
            current = current.next
            index +=1
        return None
    def get(self, index):
        """Get the node at the specified index in the linked list.
        
        Args:
            index: The position of the node to retrieve.
        
        Returns:
            Node: The node at the specified index, or None if not found.
        """
        current = self.head
        if index < 0 or index >= self.length:
            return None
        for _ in range(index):
            if current is None:
                return None
            current = current.next
        return current
            
    def set(self,index,value):
        """Set the value of the node at the specified index in the linked list.
        
        Args:
            index: The position of the node to update.
            value: The new value to set for the node.
        """
        current = self.get(index)
        current.data = value
        return current
    
    def pop_first(self):
        """Remove and return the first node in the linked list."""
        if self.head is None:
            raise IndexError("Linked list is empty")
        if self.length == 1:
            popped_node = self.head
            popped_node.next = None
            self.head = None
            self.tail = None 
        else:
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
        self.length -=1
        return popped_node
    
    def pop(self):
        "Remove and return the last tail node in the linked list"
        temp = self.head
        if self.head is None:
            raise IndexError("Linked list is empty")
        if self.length == 1:
           popped_node = self.head
           self.head = None
           self.tail = None
        else:
            while temp.next is not self.tail:
                temp = temp.next
            popped_node = self.tail
            self.tail = temp
            self.tail.next = None
        popped_node.next = None
        self.length -=1
        return popped_node
        
    def remove(self,index):
        """_summary_

        Args:
            index (_type_): _description_
        """
        if index ==0:
            return self.pop_first()
        elif index >= self.length:
            return None
        elif index == self.length -1 or index ==-1:
            return self.pop()
        else:
            prev_node = self.get(index-1)
            popped_node = prev_node.next
            prev_node.next = popped_node.next
            popped_node.next = None
            self.length -= 1 
            return popped_node 
   
    def remove1(self,index):
        if self.head is None and self.tail is None:
            return None
        #Handle single-node case
        elif self.length==1 and index==0:
            popped_node = self.head
            self.head = None
            self.tail = None
            self.length-=1
            return popped_node
        #Handle head removal
        elif index ==0:
            deleted_node = self.head
            self.head = self.head.next
            deleted_node.next = None
            self.length -=1
            return deleted_node
        elif index <0 or index >=self.length:
            self.length = 0
            return None
        #Handle pop method
        elif index == self.length-1:
            prev_node = self.head
            for _ in range(index-1):
                prev_node = prev_node.next
            popped_node = self.tail
            self.tail = prev_node
            prev_node.next = None
            self.length -=1
            return prev_node
        else:
            #find the previous node of the current index and point previous node to next of current
            prev_node = self.head
            for _ in range(index-1):
                prev_node = prev_node.next
            popped_node = prev_node.next
            prev_node.next = popped_node.next
            popped_node.next = None
            self.length -=1
            return popped_node
    
    def reverse(self):
        prev = None
        curr_copy = self.head
        curr = self.head
        while curr:
            # if curr.next == None:
            #     self.head = curr
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # self.tail = curr_copy
        self.head, self.tail = self.tail, self.head
        return prev

    def remove_duplicates(self):
        seen = set()
        prev = Node(None)
        current_node = self.head
        prev.next = current_node
        if not self.head:
            return None
        while current_node:
            if current_node.data in seen:
                prev.next = current_node.next
                self.length -=1
            else:
                seen.add(current_node.data)
                prev = prev.next
            current_node = current_node.next   
        self.tail = current_node
      
    def mergeTwoLists(self, l1, l2):
            """
            :type list1: Optional[ListNode]
            :type list2: Optional[ListNode]
            :rtype: Optional[ListNode]
            """
            d_node = Node()
            while l1 and l2:
                if l1.val < l2.val:
                    d_node.next = l1
                    l1 = l1.next
                else:
                    d_node.next = l2
                    l2 = l2.next
                d_node = d_node.next

    def removeElements(self, head, val):
        # TODO
        dummy = Node()
        dummy.next = head
        prev = dummy
        current = head
        while current:
            if current.val == val:
                prev.next = current.next
            else:
                prev = current
            current = current.next
        return dummy.next

    def reverseList(self, head):
        prev = None
        current = head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        return current

# new_list = LinkedList()
# new_list.insert(0,60)
# new_list.prepend(10)
# new_list.append(20)
# new_list.append(30)
# new_list.insert(0, 50)
# new_list.traverse()
# new_list.search(30)
# print(new_list)  # Output: 10 -> 15 -> 20 -> 30
# print(new_list.get(2))  # Output: 20
# new_list.set(2, 55)
# print(new_list)  # Output: 25
# new_list.pop_first()
# print(new_list)
# new_list.pop_first()
# print(new_list)
# new_list.pop()
# print(new_list)
# new_list.remove(6)
# new_list.remove1(0)

# new_list.reverse()
# print(new_list)
ll = LinkedList()
# 1 -> 2 -> 2 -> 3 -> 4 -> 4 -> 4 -> 5
ll.append(1)
ll.append(2)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(4)
ll.append(4)
ll.append(5)
print(ll)
ll.remove_duplicates()
print(ll)