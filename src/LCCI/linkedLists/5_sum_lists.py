"""
Sum Lists: You have two numbers represented by a linked list, where each node contains a single digit.
The digits are stored in reverse order, such that the 1 's digit is at the head of the list. 
Write a function that adds the two numbers and returns the sum as a linked list.
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Core idea - Add the digits like elementary-school addition, one place-value at a time, 
using the digit order the list already gives you (ones digit first). 
At each step, sum the two current digits plus any carry from the previous step — the new digit is sum % 10, and the new carry is sum // 10. Keep 
going until both lists are exhausted and there's no leftover carry, since a trailing carry (e.g. 5 + 5) needs one extra digit at the end.
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum = val1 + val2 + carry
            carry = sum // 10
            node = ListNode(val= sum%10)
            curr.next = node
            curr = node
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return dummy.next





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
 
    # 1. Classic example: 342 + 465 = 807
    l1 = build_linked_list([2, 4, 3])
    l2 = build_linked_list([5, 6, 4])
    result = solution.addTwoNumbers(l1, l2)
    check("classic_example", linked_list_to_array(result), [7, 0, 8])
 
    # 2. Trailing carry: 5 + 5 = 10
    l1 = build_linked_list([5])
    l2 = build_linked_list([5])
    result = solution.addTwoNumbers(l1, l2)
    check("trailing_carry", linked_list_to_array(result), [0, 1])
 
    # 3. Cascading carries: 999 + 1 = 1000
    l1 = build_linked_list([9, 9, 9])
    l2 = build_linked_list([1])
    result = solution.addTwoNumbers(l1, l2)
    check("cascading_carries", linked_list_to_array(result), [0, 0, 0, 1])
 
    # 4. Different lengths, no carry: 12 + 3 = 15
    l1 = build_linked_list([2, 1])
    l2 = build_linked_list([3])
    result = solution.addTwoNumbers(l1, l2)
    check("different_lengths", linked_list_to_array(result), [5, 1])
 
    # 5. Both zero
    l1 = build_linked_list([0])
    l2 = build_linked_list([0])
    result = solution.addTwoNumbers(l1, l2)
    check("both_zero", linked_list_to_array(result), [0])
 
    print(f"\n{passed} passed, {failed} failed")
    return failed == 0
 
 
if __name__ == "__main__":
    import sys
    success = run_tests()
    sys.exit(0 if success else 1)