from typing import TypeVar, Hashable

import random
random.seed(42)
pearson_table = list(range(256))
random.shuffle(pearson_table)

class SmartLookupTable[K: Hashable, T]:
    """Okay, it's a hash table!
    Of course, IRL we'd use a dictionary!"""
    SIZE: int
    table: list[T | None]

    def __init__(self):
        self.SIZE = 256
        self.table = [[] for _ in range(self.SIZE)]
        # ensure you understand why not this:
        # [[]] * self.SIZE



    def p_hash(self, key):
        key = bytes(key, encoding='utf8')
        hash_ = 0
        for b in key:
            hash_ = pearson_table[hash_ ^ b]
        return hash_

    def _hash(self, key: K) -> int:
        key = str(key)
        if len(key) == 0:
            raise ValueError
        return sum(map(ord, key)) % self.SIZE

    def insert(self, key: K, value: T) -> None:
        position = self._hash(key)
        self.table[position].append((key, value))



    def _find_matching_key(self, target: K, candidates: list) -> int:
        # note - use candidates.index(target)
        # this is to illustrate the sequential traversal
        # typical when using chaining with hash tables
        for i, (k, *_) in enumerate(candidates):
            if k == target:
                return i
        raise KeyError(
            f"Matching key {target} not found")
    def get(self, key: K) -> T:
        position = self._hash(key)
        keys = self.table[position]
        if not keys:
            raise KeyError(f"Matching key {key} not found")

        return keys[
            self._find_matching_key(key, keys)]


if __name__ == '__main__':
    ht = SmartLookupTable()
    ht.insert("Avigad", (45, 60, 70))
    ht.insert("Ait", (99, 100, 100))
    ht.insert("tiA", (99, 100, 100))
    ht.insert("Vishal", (99, 90, 80))
    try:
        ht.get("no one")
    except KeyError:
        print("value not found")
    print(ht.get("Avigad"))
    print(ht.get("Vishal"))
    print(ht.get("Ait"))
    print("Not so good hash:")
    print(ht._hash("aaaaaa"))
    print(ht._hash("aaaaab"))
    print(ht._hash("baaaaa"))

    print("Pearsons:")
    print(ht.p_hash("aaaaaa"))
    print(ht.p_hash("aaaaab"))
    print(ht.p_hash("baaaaa"))






