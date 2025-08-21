# DFS (stack; follows branch depth)
# [Slide: Depth Tree Search] (DFS)
def dfs_search(graph, start_node, goal_node):
    """Return True if target is reachable from start_node using DFS."""
    if start_node == goal_node:
        return True
    visited_nodes = set()
    # manual stack example
    stack = [start_node]
    while stack:
        current_node = stack.pop()
        if current_node in visited_nodes:
            continue
        visited_nodes.add(current_node)
        for neighbor in graph.get(current_node, []):
            if neighbor == goal_node:
                return True
            if neighbor not in visited_nodes:
                stack.append(neighbor)
    return False