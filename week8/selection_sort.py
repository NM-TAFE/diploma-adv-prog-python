import random
from typing import Sequence, MutableSequence
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


def sort_values(values: list[int]) -> list[int]:
    """Returns a sorted list"""
    sorted_list = []
    while values:
        index, _ = find_smallest_index_and_value(values)
        sorted_list.append(values.pop(index))
    return sorted_list


def sort_values_2(values: MutableSequence[int]) -> None:
    """Returns a sorted list"""
    sorted_list = []
    while values:
        index, value = find_smallest_index_and_value(values)
        sorted_list.append(value)
        values.remove(value)
    values.extend(sorted_list)
    return None



def recursive_sort(values):
    if len(values) <= 1:
        return values
    _, min_val = find_smallest_index_and_value(values)
    values.remove(min(values))
    return [min_val] + recursive_sort(values)


def test():
    unsorted = create_unsorted_list(100, 5)
    index, smallest = find_smallest_index_and_value(unsorted)
    assert smallest == min(unsorted), f"didn't get the smallest, {unsorted} {smallest} / {min(unsorted)}"
    assert index == unsorted.index(smallest)
    print(f"Smallest in {unsorted} is {smallest} in {index}")
    the_list = sort_values_2(unsorted)
    assert sorted(unsorted) == the_list, f"{the_list}" # == recursive_sort(unsorted), f"{recursive_sort(unsorted)}"


if __name__ == '__main__':
    test()
