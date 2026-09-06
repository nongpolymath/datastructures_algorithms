'''
# Palindrome: Implement a function to check if a linked list is a palindrome.
Core idea - 
Find the middle with slow/fast pointers, so you know where to split the list into two halves.
Reverse the second half in place — this literally flips its direction, so walking it forward now reads the original list backward.
Walk both halves forward simultaneously, comparing values pair by pair. If every pair matches, it's a palindrome.
'''
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast , slow = head , head
        # find the middle
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse second half
        prev, curr = None, slow
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # compare both halves
        left , right = head , prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

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
 
    # 1. Even-length palindrome
    head = build_linked_list([1, 2, 2, 1])
    check("even_length_palindrome", solution.isPalindrome(head), True)
 
    # 2. Odd-length palindrome
    head = build_linked_list([1, 2, 3, 2, 1])
    check("odd_length_palindrome", solution.isPalindrome(head), True)
 
    # 3. Even-length, not a palindrome
    head = build_linked_list([1, 2, 3, 4])
    check("even_length_non_palindrome", solution.isPalindrome(head), False)
 
    # 4. Odd-length, not a palindrome
    head = build_linked_list([1, 2, 3, 4, 5])
    check("odd_length_non_palindrome", solution.isPalindrome(head), False)
 
    # 5. Single-node list (always a palindrome)
    head = build_linked_list([7])
    check("single_node_list", solution.isPalindrome(head), True)
 
    # 6. Two identical nodes
    head = build_linked_list([9, 9])
    check("two_identical_nodes", solution.isPalindrome(head), True)
 
    # 7. Two different nodes
    head = build_linked_list([1, 2])
    check("two_different_nodes", solution.isPalindrome(head), False)
 
    # 8. All same value (long list)
    head = build_linked_list([5, 5, 5, 5, 5])
    check("all_same_value", solution.isPalindrome(head), True)
 
    # 9. Mismatch only in the very first pair (should short-circuit correctly)
    head = build_linked_list([9, 2, 3, 2, 1])
    check("mismatch_first_pair", solution.isPalindrome(head), False)
 
    print(f"\n{passed} passed, {failed} failed")
    return failed == 0
 
 
if __name__ == "__main__":
    import sys
    success = run_tests()
    sys.exit(0 if success else 1)