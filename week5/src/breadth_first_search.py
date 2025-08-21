# BFS (queue; level‑order)
# [Slide: Breadth Tree Search] (BFS)
# Visit nodes level-by-level from the root using a queue.
# Use an adjacency list dict[Any, list[Any]] - https://www.cs.usfca.edu/~galles/visualization/BFS.html (choose adjacency list)
from collections import deque

def bfs_search(graph, start_node, goal_node):
    """Return True if goal is reachable from start_node using BFS."""
    if start_node == goal_node:
        return True
    visited_nodes = set([start_node])
    queue = deque([start_node])
    while queue:
        current_node = queue.popleft()
        for neighbor in graph.get(current_node, []):
            if neighbor == goal_node:
                return True
            if neighbor not in visited_nodes:
                visited_nodes.add(neighbor)
                queue.append(neighbor)
    return False