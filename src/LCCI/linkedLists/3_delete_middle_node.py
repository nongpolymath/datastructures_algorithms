"""
Delete Middle Node: Implement an algorithm to delete a node in the middle 
(i.e., any node but the first and last node, not necessarily the exact middle)
 of a singly linked list, given only access to that node.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def delete_mid_node(self, node):
        if node is None or node.next is None:
            return False
        node.val = node.next.val
        node.next = node.next.next
        return True



# ---------------------------------------------------------------------------
# Test harness helpers
# ---------------------------------------------------------------------------
 
def build_linked_list(values):
    """Build a singly linked list from `values` and return a list of the
    actual ListNode objects (in order), so tests can grab a direct reference
    to any node -- mirroring the problem's constraint of "only access to
    that node"."""
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    return nodes
 
 
def linked_list_to_array(head):
    values = []
    while head is not None:
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
 
    # 1. Delete a true middle node
    nodes = build_linked_list([1, 2, 3, 4, 5])
    result = solution.delete_mid_node(nodes[2])  # delete value 3
    check("delete_true_middle_node -> return", result, True)
    check("delete_true_middle_node -> list", linked_list_to_array(nodes[0]), [1, 2, 4, 5])
 
    # 2. Delete the second-to-last node
    nodes = build_linked_list([1, 2, 3])
    result = solution.delete_mid_node(nodes[1])  # delete value 2
    check("delete_second_to_last -> return", result, True)
    check("delete_second_to_last -> list", linked_list_to_array(nodes[0]), [1, 3])
 
    # 3. Delete the first node (algorithm doesn't care it's "first")
    nodes = build_linked_list([1, 2, 3, 4])
    result = solution.delete_mid_node(nodes[0])
    check("delete_first_node -> return", result, True)
    check("delete_first_node -> list", linked_list_to_array(nodes[0]), [2, 3, 4])
 
    # 4. Cannot delete the last node
    nodes = build_linked_list([1, 2, 3])
    result = solution.delete_mid_node(nodes[2])
    check("cannot_delete_last_node -> return", result, False)
    check("cannot_delete_last_node -> list unchanged", linked_list_to_array(nodes[0]), [1, 2, 3])
 
    # 5. Single-node list
    nodes = build_linked_list([42])
    result = solution.delete_mid_node(nodes[0])
    check("single_node_list -> return", result, False)
    check("single_node_list -> list unchanged", linked_list_to_array(nodes[0]), [42])
 
    # 6. None input
    result = solution.delete_mid_node(None)
    check("none_node -> return", result, False)
 
    # 7. Two-node list, delete the first
    nodes = build_linked_list([1, 2])
    result = solution.delete_mid_node(nodes[0])
    check("two_node_list_delete_first -> return", result, True)
    check("two_node_list_delete_first -> list", linked_list_to_array(nodes[0]), [2])
 
    print(f"\n{passed} passed, {failed} failed")
    return failed == 0
 
 
if __name__ == "__main__":
    import sys
    success = run_tests()
    sys.exit(0 if success else 1)