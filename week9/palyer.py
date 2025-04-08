from __future__ import annotations
import random
import unittest
sorted([1, 2, 3, 4], reverse=True)
class Player:
    def __init__(self, id, name, score):
        ...

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}({self.id!r}, "
    @classmethod
    def sort(cls, players: list[Player]) -> list[Player]:
        if len(players) <= 1:
            return players
        pivot = players[0]
        left = []
        right = []
        for player in players[1:]:
            if player < pivot:
                left.append(player)
            else:
                right.append(player)
        return cls.sort(left) + [pivot] + cls.sort(right)
