class PlayerList: ...


class PlayerHashTable:
    SIZE = 42
    hash_map: list[PlayerList]

    def __init__(self):

        self.hash_map = [PlayerList() for _ in range(self.SIZE)]

