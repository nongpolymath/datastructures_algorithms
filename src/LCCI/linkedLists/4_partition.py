'''
Partition: Write code to partition a linked list around a value x, 
such that all nodes less than x come before all nodes greater than or equal to x.
lf x is contained within the list, the values of x only need to be after the elements less than x (see below). 
The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.
'''

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        curr = head
        less_dummy = ListNode()
        more_dummy = ListNode()
        less , more = less_dummy , more_dummy
        while curr:
            if curr.val < x:
                less.next = curr
                less = curr
            else:
                more.next = curr
                more = curr
            curr = curr.next
        less.next = more_dummy.next
        more.next = None
        return less_dummy.next


# ---------------------------------------------------------------------------
# Test harness helpers
# ---------------------------------------------------------------------------
 
def build_linked_list(values):
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next
 
 
def linked_list_to_array(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values
 
 
# ---------------------------------------------------------------------------
# Simple test harness (no framework, just asserts + a runner)
# ---------------------------------------------------------------------------
 
def run_tests():
    solution = Solution()
    passed = 0
    failed = 0
 
    def check(name, actual, expected):
        nonlocal passed, failed
        if actual == expected:
            print(f"PASS  {name}")
            passed += 1
        else:
            print(f"FAIL  {name}  (expected {expected!r}, got {actual!r})")
            failed += 1
 
    # 1. Classic LeetCode example
    head = build_linked_list([1, 4, 3, 2, 5, 2])
    result = solution.partition(head, 3)
    check("classic_example", linked_list_to_array(result), [1, 2, 2, 4, 3, 5])
 
    # 2. All nodes already less than x
    head = build_linked_list([1, 2, 3])
    result = solution.partition(head, 10)
    check("all_less_than_x", linked_list_to_array(result), [1, 2, 3])
 
    # 3. All nodes greater than or equal to x
    head = build_linked_list([5, 6, 7])
    result = solution.partition(head, 1)
    check("all_greater_equal_x", linked_list_to_array(result), [5, 6, 7])
 
    # 4. x not present in the list at all
    head = build_linked_list([9, 1, 8, 2, 7])
    result = solution.partition(head, 5)
    check("x_not_in_list", linked_list_to_array(result), [1, 2, 9, 8, 7])
 
    # 5. Single-node list
    head = build_linked_list([1])
    result = solution.partition(head, 0)
    check("single_node_list", linked_list_to_array(result), [1])
 
    # 6. Empty list
    head = build_linked_list([])
    result = solution.partition(head, 3)
    check("empty_list", linked_list_to_array(result), [])
 
    # 7. Duplicate values equal to x (should all land in the "more" bucket)
    head = build_linked_list([3, 3, 3])
    result = solution.partition(head, 3)
    check("all_equal_to_x", linked_list_to_array(result), [3, 3, 3])
 
    print(f"\n{passed} passed, {failed} failed")
    return failed == 0
 
 
if __name__ == "__main__":
    import sys
    success = run_tests()
    sys.exit(0 if success else 1)