from __future__ import annotations
from typing import TYPE_CHECKING
from player_node import PlayerNode

if TYPE_CHECKING:
    # from player_node import PlayerNode
    from player import Player


class PlayerList:
    head: None | PlayerNode
    tail: None | PlayerNode

    def __init__(self,
                 _head=None,
                 _tail=None,
                 _players: list[Player] | None = None):

        self.head = _head
        self.tail = _tail

        if _players:
            for player in _players:
                self.append(player)

    def append(self, player: Player) -> None:
        new_node = PlayerNode(player)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next_node = new_node
        new_node.prev_node = self.tail
        self.tail = new_node

    def search(self, key: str) -> PlayerNode:
        if self.head is None:
            raise ValueError("List is empty")

        current_node = self.head
        while current_node is not None:
            if current_node.key == key:
                return current_node
            current_node = current_node.next_node

        raise ValueError(f"{key = } not found")