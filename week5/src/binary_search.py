# 2) Binary Search (requires sorted data)
# [Slide: Binary search]
# Requires sorted data. 

# Iterative
def binary_search_iter(needle, haystack):
    """Return index of needle in sorted haystack or -1 if not found."""
    left, right = 0, len(haystack) - 1
    # Compares the middle element; halves the search space each step.
    while left <= right:
        mid_point = (left + right) // 2
        if haystack[mid_point] == needle:
            return mid_point
        if haystack[mid_point] < needle:
            left = mid_point + 1
        else:
            right = mid_point - 1
    return -1

# Recursive
def binary_search_rec(needle, haystack, left=0, right=None):
    """Return index of needle in sorted haystack or -1 if not found."""
    if right is None:
        right = len(haystack) - 1
    if left > right:
        return -1
    mid_point = (left + right) // 2
    if haystack[mid_point] == needle:
        return mid_point
    if haystack[mid_point] < needle:
        return binary_search_rec(needle, haystack, mid_point + 1, right)
    else:
        return binary_search_rec(needle, haystack, left, mid_point - 1)