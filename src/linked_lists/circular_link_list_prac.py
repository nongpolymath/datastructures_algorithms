class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
    def __str__(self):
        """
        Returns the string representation of the node's value.

        Returns:
            str: The value of the node as a string.
        """
        return f"Node value {str(self.value)}"
        
class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        """
        Returns a string representation of the circular linked list.

        Iterates through the nodes starting from the head, appending each node's value to a string,
        separated by ' -> '. Stops when it loops back to the head node, indicating the circular nature.
        If the list is empty, returns an empty string.

        Returns:
            str: A string showing the sequence of node values in the circular linked list.
        """
        current = self.head
        result = ''
        if self.length == 0:
            return result
        else:
            while current is not None:
                result = result + str(current.value)+" -> "
                current= current.next
                if current is self.head:
                    break
            return result[:-4]             
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length +=1
        
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length +=1
        return new_node
    
    def insert(self, value: int, index: int) -> Node:
        new_node = Node(value)
        if index < 0 or index > self.length:
            raise IndexError(f"Index {index} out of bounds for list of length {self.length}.")
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        if index == 0:
            return self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            nxt = curr.next
            curr.next = new_node
            new_node.next = nxt
        self.length += 1
        return new_node
            
    def traverse(self):
        """
        Traverses the circular linked list and prints the values of all nodes in order.
        Returns:
            str: A string containing the values of all nodes in the list, separated by spaces.
        """
        
        curr = self.head
        result = ''
        while curr is not None:
            result += str(curr.value)+" "
            curr = curr.next
            if curr==self.head:
                break
        print(result)
        return result
    
    def search(self, target: int) -> 'Node | None':
        """
        Searches for a node with the specified value in the circular linked list.

        Args:
            target: The value to search for in the list.

        Returns:
            The node containing the specified value if found, otherwise None.
        """
        if self.head is None: return None
        curr = self.head
        while curr is not None:
            if curr.value == target:
                print(f"target value found at {curr} with value {curr.value}")
                return curr
            curr = curr.next
            if curr == self.head:
                break
            
    def get(self, index: int) -> Node | None:
        """
        Retrieve the value of the node at the specified index in the circular linked list.

        Args:
            index (int): The position of the node to retrieve, where 0 is the head of the list.

        Returns:
            Node | None: The node at the specified index, or None if the index is out of bounds.
        """
        curr = self.head
        if self.head is None: return None
        if index <0 or index>self.length:
            raise IndexError(f"Provided index is out range of the Circular Linked List with length {self.length}")
        for _ in range(index):
            curr = curr.next          
        return curr
    
    def set(self, index: int, value: object) -> None:
        """
        Sets the value of the node at the specified index in the circular linked list.

        Args:
            index (int): The position of the node to update.
            value (Any): The new value to assign to the node.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if self.head is None:
            return None
        if index< 0 or index> self.length:
            raise IndexError()
        current = self.head
        for _ in range(index):
            current = current.next
        current.value = value
        return current            
    
    def pop_first(self):
        """
        Removes and returns the first node from the circular linked list.

        Returns:
            The data stored in the removed node, or None if the list is empty.

        Raises:
            Exception: If the list is empty.
        """
        if self.head is None:
            raise ValueError
        elif self.length==1:
            popped_node = self.head
            self.head = None
            self.tail = None            
        else:    
            popped_node = self.head
            self.head = self.head.next
            self.tail.next = self.head
        popped_node.next = None
        self.length -=1
        return popped_node
    
    def pop(self):
        """
        Removes and returns the last node from the circular linked list.

        Returns:
            The data stored in the removed node.

        Raises:
            IndexError: If the list is empty.
        """
        if self.head is None and self.length==0:
            return IndexError("pop from empty list")
        elif self.length ==1:
            popped_node = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return popped_node.value
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            popped_node = current.next
            current.next = self.head
            self.tail = current
            self.length -=1
            return popped_node.value
        
        
    def remove(self,index):
        """
        Removes the node at the specified index from the circular linked list.

        Args:
            index (int): The position of the node to remove. Indexing starts at 0.

        Raises:
            IndexError: If the index is out of range.

        Returns:
            The data stored in the removed node.
        """
        if self.head is None:
            raise IndexError("empty list")
        elif index<0 or index>self.length:
            raise IndexError("index exceeded length of circular linked list")
        elif index == 0:
            return self.pop_first()
        elif index == self.length-1:
            return self.pop()
        else:
            prev = self.head
            for _ in range(index-1):
                prev = prev.next
            popped_node = prev.next
            prev.next = popped_node.next
            popped_node.next = None
            self.length -=1
            return popped_node.value
        
    def remove_node(self, node):
        """
        Removes the specified node from the circular linked list.

        Parameters:
            node: The node to be removed from the list.

        Raises:
            ValueError: If the node is not found in the list.
        """
        if self.head is None:
            raise IndexError("empty list")
        elif node == self.head:
            return self.pop_first()
        elif node == self.tail:
            return self.pop()
        else:
            prev = self.head
            while prev.next != node:
                prev = prev.next
            popped_node = prev.next
            prev.next = popped_node.next
            popped_node.next = None
            self.length -=1
            return popped_node
        
    def delete_all(self):
        """
        Removes all nodes from the circular linked list, resulting in an empty list.

        This method traverses the entire circular linked list and deletes all its nodes,
        resetting the list to its initial empty state.
        """
        self.tail.next = None
        self.head = None
        self.tail = None
        self.length = 0

    def split_list(self):
        if not self.head or self.head.next == self.head:
            return self.head, None
        
        fast = self.head
        slow = self.head
        while fast.next != self.head and fast.next.next !=self.head:
            fast = fast.next.next
            slow = slow.next

        #move fast to end if even circular linked list
        if fast.next.next == self.head:
            fast = fast.next
            
        head1 = self.head
        head2 = slow.next
        
        slow.next = head1
        fast.next = head2
        # print the two split lists
        curr = head1
        result = ''
        while curr != None:
            result += str(curr.value)
            result += " -> "
            curr = curr.next
            if curr == head1:
                break
        print(result[:-4])
        curr2 = head2
        result2 = ''
        while curr2 != None:
            result2 += str(curr2.value)
            result2 += " -> "
            curr2 = curr2.next
            if curr2 == head2:
                break
        print(result2[:-4])
        return head1,head2

    def is_sorted(self):
        if self.head is None or self.head.next == self.head:
            return True #Empty or single linked circular list
        current = self.head
        flag = 0
        while True:
            if current.value > current.next.value:
                flag += 1
                if flag>1:
                    return False
            else:
                current = current.next
            if current.next == self.head:
                break
        return True
    
    def josephus_circle(self,step):
        """
        Solves the Josephus problem using a circular linked list.

        The Josephus problem is a theoretical problem related to a certain elimination game.
        People are standing in a circle waiting to be executed. Counting begins at a specified point in the circle
        and proceeds around the circle in a specified direction. After a specified number of people are skipped,
        the next person is executed. The procedure is repeated with the remaining people, starting with the next person,
        going around the circle, and skipping the same number of people, until only one person remains, who is given freedom.

        Args:
            step (int): The number of people to skip before eliminating the next person.

        Returns:
            Any: The data of the last remaining node/person in the circle.
        """
        curr = self.head
        while self.length>1:
            count = 1
            while count != step:
                count +=1
                curr = curr.next
            temp = curr.next
            self.remove_node(curr)
            print(self)
            curr = temp

cs_ll = CSLinkedList()
cs_ll.append(10)
cs_ll.append(20)
cs_ll.append(30)
cs_ll.append(40)
cs_ll.append(50)
cs_ll.append(60)
cs_ll.prepend(3)
print(cs_ll)
cs_ll.insert(25,3)
print(cs_ll)
cs_ll.traverse()
cs_ll.search(30)
print(cs_ll.set(7,65))
print(cs_ll)
#cs_ll.split_list()
print(cs_ll.is_sorted())
print(cs_ll.josephus_circle(2))
print(cs_ll)
# print(cs_ll.pop_first().value)
# print(cs_ll)
# #cs_ll.pop()
# print(cs_ll.remove(4))
# print(cs_ll.tail.value)