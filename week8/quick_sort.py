import random

class Player:

    def __init__(self, score = None):
        self.score = score or random.randint(0, 100)

    def __lt__(self, other):
        return self.score < other.score

    def __ge__(self, other):
        return self.score >= other.score

    def __eq__(self, other):
        return self.score == other.score

    def __repr__(self):
        class_name = self.__class__.__name__
        return f"{class_name}({self.score!r})"

def raf_sort(arr):
    arr.sort()

def quicksort(arr):
    if len(arr) <= 1:
        return arr # base case
    pivot = arr[0]
    left = [i for i in arr[1:] if i < pivot]
    right = [i for i in arr[1:] if i >= pivot]
    return (quicksort(left)
            + [pivot]
            + quicksort(right))

players = [Player() for _ in range(10)]
# print(quicksort(players))
# print(players)
raf_sort(players)
print(players)

random.seed(42)
random_scores = random.sample(range(1000), 1000)
players = [Player(i) for i in random_scores]

presorted_players = sorted(players)
raf_sort(players)
assert players == presorted_players