import random
from typing import Sequence
from functools import lru_cache


def create_unsorted_list(max_val: int,
                         length: int,
                         min_val: int = 0) -> list[int]:
    return [random.randint(min_val, max_val) for _ in range(length)]


def find_smallest_index_and_value(values: Sequence[int]) -> tuple[int, int]:
    """Given a sequence returns index and value"""
    smallest = values[0]
    smallest_index = 0
    for index, value in enumerate(values[1:], 1):
        if value < smallest:
            smallest = value
            smallest_index = index
    return smallest_index, smallest


def test():
    unsorted = create_unsorted_list(100, 5)
    index, smallest = find_smallest_index_and_value(unsorted)
    assert smallest == min(unsorted), f"didn't get the smallest, {unsorted} {smallest} / {min(unsorted)}"
    assert index == unsorted.index(smallest)
    print(f"Smallest in {unsorted} is {smallest} in {index}")


if __name__ == '__main__':
    test()
