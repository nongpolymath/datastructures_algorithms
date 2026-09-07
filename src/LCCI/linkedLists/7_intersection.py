"""
Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node. 
Note that the intersection is defined based on reference, not value. That is, 
if the kth node of the first linked list is the exact same node (by reference) as the jth node of the second linked list, 
then they are intersecting.
Approach 1 — measure and offset. Get the length of each list. Whichever list is longer, advance its pointer forward by the length difference first 
(2 nodes ahead in list A's case, if B were longer by 2). Now both pointers are the same distance from the end. 
Walk them forward together one step at a time, comparing by reference (is, not ==) — the first node where they match is the intersection.

Approach 2 — the elegant swap trick (no length calculation needed). Run two pointers, pA starting at headA and pB starting at headB. 
When either pointer reaches the end of its list, redirect it to the head of the other list instead of stopping.
Keep advancing both one step at a time until they point to the same node.

"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNodeOffset(self, headA, headB):
    # measure length of the linked lists
    l1 , l2 = 0, 0
    currA , currB = headA, headB
    while currA:
        l1 += 1
        currA = currA.next
    while currB:
        l2 += 1
        currB = currB.next
    currA , currB = headA, headB
    if l1 > l2:
        for _ in range(l1- l2):
            currA = currA.next
    else:
        for _ in range(l2-l1):
            currB = currB.next

    while currA and currB and currA != currB:
        currA = currA.next
        currB = currB.next
    return currA

def getIntersectionNodeSwap(self, headA, headB):
    p1 , p2 = headA, headB
    while p1 != p2:
        p1 = p1.next if p1 else headB
        p2 = p2.next if p2 else headA
    return p1





# ---------------------------------------------------------------------------
# Test harness helpers
# ---------------------------------------------------------------------------
 
def build_chain(values):
    """Build a simple chain of nodes from values and return a list of the
    actual ListNode objects, so we can grab a direct reference to any node
    (e.g. to splice a shared tail onto two separate prefixes)."""
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    return nodes
 
 
def make_intersecting_lists(a_unique_vals, b_unique_vals, shared_vals):
    """Build two lists that share a common tail. Returns (headA, headB, shared_head_node)."""
    a_nodes = build_chain(a_unique_vals) if a_unique_vals else []
    b_nodes = build_chain(b_unique_vals) if b_unique_vals else []
    shared_nodes = build_chain(shared_vals)
 
    if a_nodes:
        a_nodes[-1].next = shared_nodes[0]
        headA = a_nodes[0]
    else:
        headA = shared_nodes[0]
 
    if b_nodes:
        b_nodes[-1].next = shared_nodes[0]
        headB = b_nodes[0]
    else:
        headB = shared_nodes[0]
 
    return headA, headB, shared_nodes[0]
 
 
# ---------------------------------------------------------------------------
# Simple test harness (no framework, just asserts + a runner)
# ---------------------------------------------------------------------------
 
def run_tests():
    passed = 0
    failed = 0
 
    def check(name, actual, expected):
        nonlocal passed, failed
        if actual is expected:
            print(f"PASS  {name}")
            passed += 1
        else:
            got_val = actual.val if actual else None
            exp_val = expected.val if expected else None
            print(f"FAIL  {name}  (expected node {exp_val!r}, got {got_val!r})")
            failed += 1
 
    def check_both(case_name, headA, headB, expected_node):
        r1 = getIntersectionNodeOffset(None, headA, headB)
        check(f"{case_name} [offset approach]", r1, expected_node)
        r2 = getIntersectionNodeSwap(None, headA, headB)
        check(f"{case_name} [swap approach]", r2, expected_node)
 
    # 1. Intersecting, unequal unique-prefix lengths
    headA, headB, shared = make_intersecting_lists([1, 2], [6, 7, 8], [3, 4, 5])
    check_both("intersecting_unequal_lengths", headA, headB, shared)
 
    # 2. Intersecting, equal unique-prefix lengths
    headA, headB, shared = make_intersecting_lists([1, 2], [6, 7], [3, 4])
    check_both("intersecting_equal_lengths", headA, headB, shared)
 
    # 3. No intersection at all, different lengths
    a_nodes = build_chain([1, 2])
    b_nodes = build_chain([9, 8, 7])
    check_both("no_intersection_diff_lengths", a_nodes[0], b_nodes[0], None)
 
    # 4. No intersection, same length
    a_nodes = build_chain([1, 2, 3])
    b_nodes = build_chain([9, 8, 7])
    check_both("no_intersection_same_length", a_nodes[0], b_nodes[0], None)
 
    # 5. Entire lists are identical (headA is headB)
    a_nodes = build_chain([1, 2, 3])
    check_both("identical_lists_full_overlap", a_nodes[0], a_nodes[0], a_nodes[0])
 
    # 6. Intersection is only the very last (tail) node
    headA, headB, shared = make_intersecting_lists([1, 2, 3], [9], [5])
    check_both("intersection_at_tail_only", headA, headB, shared)
 
    # 7. One list has no unique prefix at all (headB IS the shared node)
    headA, headB, shared = make_intersecting_lists([1, 2], None, [5, 6])
    check_both("empty_unique_prefix_on_b", headA, headB, shared)
 
    print(f"\n{passed} passed, {failed} failed")
    return failed == 0
 
 
if __name__ == "__main__":
    import sys
    success = run_tests()
    sys.exit(0 if success else 1)