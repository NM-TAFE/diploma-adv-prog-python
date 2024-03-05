from typing import TYPE_CHECKING

from player_list import PlayerList
from player import Player

class PlayerHashTable:
    SIZE = 42
    hash_map: list[PlayerList]

    def __init__(self):
        self.hash_map = [PlayerList()] * self.SIZE

    def get_index(self, hash_: int):
        return hash_ % self.SIZE

    def __getitem__(self, key: str) -> Player:
        """Return a player by key"""
        index = self.get_index(Player.make_hash(key))
        player_list = self.hash_map[index]
        try:
            player_node = player_list.search(key)
            return player_node.player

        except ValueError as e:
            raise KeyError(str(e))



    def __setitem__(self, id, name):
        """Behave like a dictionary such that:
        >>> phash = PlayerHashTable()
        >>> phash[42] = "Raf"

        Shall create a player Raf with uid 42
        """
        player = Player(id, name)
        index = self.get_index(hash(player))
        player_list = self.hash_map[index]
        try:
            node = player_list.search(id)
            node.player = player
        except ValueError:
            player_list.append(player)


        # hash the player
        # see if player in list
        # if yes, replace player
        # else append player
def main():
    ph = PlayerHashTable()
    ph['1'] = 'Raf'
    ph['2'] = 'Faf'
    print(ph['1'])
    # ph['42']

if __name__ == '__main__':
    main()