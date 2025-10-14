from collections import namedtuple

def format_bst(sorted_vals):
    """
    Accepts a sorted list of ints and returns a formatted ASCII BST.
    Produces a height-balanced BST (minimal height).
    """

    # --- 1) Build a minimal-height BST from the sorted array ---
    Node = namedtuple("Node", "val left right")
    def build(lo, hi):
        if lo > hi:
            return None
        mid = (lo + hi) // 2
        return Node(sorted_vals[mid], build(lo, mid - 1), build(mid + 1, hi))
    root = build(0, len(sorted_vals) - 1)
    if not root:
        return ""

    # --- 2) Pretty-print the tree into ASCII ---
    # The display() function returns (lines, width, height, root_x)
    # Adapted from a common recursive composition approach.
    n
    def display(node):
        if node is None:
            return [""], 0, 0, 0

        s = str(node.val)
        left_lines, left_w, left_h, left_x = display(node.left)
        right_lines, right_w, right_h, right_x = display(node.right)

        # Pad shorter side
        height = max(left_h, right_h)
        left_lines += [" " * left_w] * (height - left_h)
        right_lines += [" " * right_w] * (height - right_h)

        # Position of current node
        # left_root is where the left root sits relative to left block
        # right_root similarly for right block
        # We’ll place this node centered between the two sub-blocks.
        val_w = len(s)

        # If no children, just return the node text
        if left_w == 0 and right_w == 0:
            return [s], val_w, 1, val_w // 2

        # First (node) row: left pad + value + right pad
        gap = 1  # minimum gap between left and right blocks
        first_row_w = left_w + gap + right_w
        # Center the value above the gap between left and right
        # Node root_x is left_w + gap//2; we’ll try to center string s there
        root_x_target = left_w + gap // 2
        # Compute left padding so that s’s center lands at root_x_target
        s_half = val_w // 2
        s_start = max(0, root_x_target - s_half)
        s_end = s_start + val_w
        # Ensure the row is wide enough
        first_row_w = max(first_row_w, s_end)
        first_row = [" "] * first_row_w
        first_row[s_start:s_end] = list(s)
        first_row = "".join(first_row)

        # Second row: connection lines from this node down to children
        # Compute where left and right child roots are located in their blocks
        left_root_x = left_x
        right_root_x = left_w + gap + right_x

        # Draw connectors only if child exists
        second_row = [" "] * first_row_w
        if node.left:
            # vertical from node down
            second_row[left_root_x] = "/"
            # extend underscores from left_root_x+1 up to just before s_start if needed
            for i in range(left_root_x + 1, s_start):
                second_row[i] = "_"
        if node.right:
            second_row[right_root_x] = "\\"
            for i in range(s_end, right_root_x):
                second_row[i] = "_"
        second_row = "".join(second_row)

        # Merge left and right blocks line-by-line with a gap between
        merged_lines = []
        for l_line, r_line in zip(left_lines, right_lines):
            merged_lines.append(l_line + " " * gap + r_line)

        lines = [first_row, second_row] + merged_lines
        width = len(lines[0])
        height = 2 + len(merged_lines)
        root_x = (s_start + s_end - 1) // 2
        return lines, width, height, root_x

    lines, *_ = display(root)
    # Strip trailing spaces on each line for a cleaner look
    return "\n".join(line.rstrip() for line in lines)


# --- Example ---
if __name__ == "__main__":
    print(format_bst(list(range(15))))
