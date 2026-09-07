"""
Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop. 
DEFINITION Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so as to make a loop in the linked list.
Approach - Use two pointers, one moving twice as fast as the other, to detect if there's a loop 
— if there is, the fast one will eventually catch up to the slow one from behind. 
Once they meet, reset one pointer back to the start of the list and move both forward one step at a time; wherever they meet the second time is exactly where the loop begins.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype
        """
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow


