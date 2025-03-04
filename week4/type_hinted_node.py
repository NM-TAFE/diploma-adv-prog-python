from __future__ import annotations

class Node:
    next_node: Node | None


    def __init__(self):
        self.value = None
        self.next_node = None