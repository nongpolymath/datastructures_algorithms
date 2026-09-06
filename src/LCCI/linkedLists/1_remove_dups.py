'''
Remove Dups: Write code to remove duplicates from an unsorted linked list. How would you solve this problem if a temporary buffer is not allowed?
'''

import threading


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O(1) space complexity
def remove_dups_no_buffer(head):
    if not head:
        return
    curr = head

    while curr:
        runner = curr
        while runner.next:
            if runner.next.val == curr.val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        curr = curr.next
    return head


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


class TimeoutError_(Exception):
    pass


class _Box:
    """Small mutable holder so the worker thread can hand a result (or
    exception) back to the main thread."""
    def __init__(self):
        self.value = None
        self.exc = None


def call_with_timeout(fn, arg, seconds=2):
    box = _Box()

    def target():
        try:
            box.value = fn(arg)
        except Exception as e:
            box.exc = e

    t = threading.Thread(target=target, daemon=True)
    t.start()
    t.join(timeout=seconds)

    if t.is_alive():
        raise TimeoutError_("function did not return -- likely an infinite loop")
    if box.exc is not None:
        raise box.exc
    return box.value


# ---------- test cases ----------

def run_case(name, input_values):
    head = list_to_linked(input_values)
    try:
        result_head = call_with_timeout(remove_dups_no_buffer, head)
    except TimeoutError_:
        raise AssertionError(f"[{name}] TIMED OUT -- function hung (infinite loop)")
    result = linked_to_list(result_head)
    expected = list(dict.fromkeys(input_values))  # first-occurrence order
    assert result == expected, f"[{name}] expected {expected}, got {result}"
    print(f"PASS  {name:35s} {input_values} -> {result}")


if __name__ == "__main__":
    run_case("empty list", [])
    run_case("single node", [5])
    run_case("no duplicates", [1, 2, 3, 4, 5])
    run_case("all same value", [7, 7, 7, 7, 7])
    run_case("duplicates scattered", [1, 2, 3, 2, 1, 4, 5, 3])
    run_case("duplicates at head", [1, 1, 2, 3])
    run_case("duplicates at tail", [1, 2, 3, 3, 3])
    run_case("two nodes, same value", [9, 9])
    run_case("two nodes, different values", [9, 8])
    run_case("negative and zero values", [0, -1, -1, 0, 2, -3])

    assert remove_dups_no_buffer(None) is None, "empty list should return None"
    print(f"PASS  {'None returned for empty list':35s}")

    print("\nAll tests passed.")