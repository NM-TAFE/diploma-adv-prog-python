# BFS (queue; level‑order)
# [Slide: Breadth Tree Search] (BFS)
# Visit nodes level-by-level from the root using a queue.
# We’ll use an adjacency list dict[Any, list[Any]].

from collections import deque

def bfs_iterative_search(graph, start_node, goal_node):
    """Return True iff goal_node is reachable from start_node using BFS."""
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

def dfs_iterative_search(graph, start_node, goal_node):
    """Return True iff goal_node is reachable from start_node using DFS."""
    if start_node == goal_node:
        return True
    visited_nodes = set()
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