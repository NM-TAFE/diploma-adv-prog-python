from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from player import Player


class PlayerNode:
    next_node: PlayerNode | None
    prev_node: PlayerNode | None

    def __init__(self, player: Player, prev_node=None, next_node=None):
        self.player = player
        self.next_node = next_node
        self.prev_node = prev_node

    @property
    def key(self):
        return self.player.uid
    