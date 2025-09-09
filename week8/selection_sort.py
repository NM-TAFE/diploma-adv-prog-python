import random
from typing import Sequence


def create_unsorted_list(max_val: int,
                         length: int,
                         min_val: int = 0) -> list[int]:
    return [random.randint(min_val, max_val) for _ in range(length)]


def get_smallest_number(values: Sequence[int]) -> int:
    smallest = values[0]
    for value in values[1:]:
        if value < smallest:
            smallest = value
    return smallest
def test():
    unsorted = create_unsorted_list(100, 10)
    smallest = get_smallest_number(unsorted)
    assert smallest == min(unsorted), "didn't get the smallest"
    print(f"Smallest in {unsorted} is {smallest}")


if __name__ == '__main__':
    test()
