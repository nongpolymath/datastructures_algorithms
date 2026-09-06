'''
# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
'''
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # using two pointer method (fast, slow). Offset fast by n+1 times from slow , move both pointers till 'fast' points to null
    def removeNthFromEnd(self, head: Optional['ListNode'], n: int) -> Optional['ListNode']:
        if not head:
            return
        dummy = ListNode(0, head)
        fast = slow = dummy
        for _ in range(n+1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next




# ---------- helpers ----------
 
def list_to_linked(values):
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next
 
 
def linked_to_list(head):
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result
 
 
# ---------- test cases ----------
 
def run_case(name, values, n, expected):
    head = list_to_linked(values)
    solver = ListNode()  # self is unused in removeNthFromEnd, any instance works
    result = linked_to_list(solver.removeNthFromEnd(head, n))
    assert result == expected, f"[{name}] values={values} n={n} expected={expected}, got={result}"
    print(f"PASS  {name:30s} values={values!r:20} n={n} -> {result}")
 
 
if __name__ == "__main__":
    run_case("remove middle node", [1, 2, 3, 4, 5], 2, [1, 2, 3, 5])
    run_case("remove only node", [1], 1, [])
    run_case("two nodes, remove second-to-last", [1, 2], 1, [1])
    run_case("two nodes, remove head", [1, 2], 2, [2])
    run_case("n equals length -- removes head", [1, 2, 3, 4, 5], 5, [2, 3, 4, 5])
    run_case("n == 1 -- removes tail", [1, 2, 3, 4, 5], 1, [1, 2, 3, 4])
 
    # empty list should return None without raising
    solver = ListNode()
    assert solver.removeNthFromEnd(None, 1) is None, "empty list should return None"
    print(f"PASS  {'None returned for empty list':30s}")
 
    print("\nAll tests passed.")