# 1) Linear Search (unsorted OK)
# [Slide: Linear search]

# Moves through each item in an array. Works with unsorted data.
# Worst case: item at end or not present; compares up to N items.
def linear_search(needle, haystack):
    """Return index if found or -1 if not found."""
    for index, value in enumerate(haystack):
        if value == needle:
            return index
    return -1

