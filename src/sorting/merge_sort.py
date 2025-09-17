from typing import List, Any

def merge_sort(customList: List[Any]) -> List[Any]:
    """
    In-place (overwrites input) recursive merge sort.

    Args:
        customList: list of comparable items to sort.

    Returns:
        The same list object, sorted in ascending order.

    Complexity:
        Time:  O(n log n) for best/average/worst.
        Space: O(n) extra (sublists via slicing); recursion depth O(log n).

    Note:
        - This implementation overwrites the original list (mutates in place),
          but still allocates left/right sublists (not an in-place-memory algorithm).
        - It's stable because the merge uses '<=' to choose left items first on ties.
    """
    # Base case: lists of length 0 or 1 are already sorted
    if len(customList) > 1:
        # 1) Divide: find midpoint and create left/right halves (slices)
        mid = len(customList) // 2
        left_half = customList[:mid]
        right_half = customList[mid:]

        # 2) Conquer: recursively sort each half
        merge_sort(left_half)
        merge_sort(right_half)

        # 3) Merge: merge sorted halves back into customList
        i = j = k = 0
        # i -> index into left_half
        # j -> index into right_half
        # k -> index into customList (where we'll write next smallest)

        # Compare elements from both halves and copy the smaller one
        # Using '<=' makes this merge stable: when values are equal, left_half wins
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                customList[k] = left_half[i]
                i += 1
            else:
                customList[k] = right_half[j]
                j += 1
            k += 1

        # If any elements remain in left_half, copy them
        while i < len(left_half):
            customList[k] = left_half[i]
            i += 1
            k += 1

        # If any elements remain in right_half, copy them
        while j < len(right_half):
            customList[k] = right_half[j]
            j += 1
            k += 1

    # Return sorted list for convenience (note: customList was modified in-place)
    return customList