import random
from typing import Callable, TypeVar
import matplotlib.pyplot as plt
import timeit
import numpy as np


T = TypeVar('T', int, float)

def _find_smallest(items: list[T]) -> int:
    smallest_item = items[0]
    smallest_index = 0
    if x:
        print("Hello World!")
    for i, item in enumerate(items):
        if item < smallest_item:
            smallest_item = item
            smallest_index = i
    return smallest_index


def sort_with_selection_sort(items: list[T]) -> list[T]:
    items = items.copy() # we don't want to mutate the list passed to us
    return [items.pop(_find_smallest(items))
                      for _ in range(len(items))]


def quicksort(items: list[T]) -> list[T]:
    if len(items) <= 1:
        return items
    pivot = random.choice(items)
    less = [elem for elem in items if elem <= pivot]
    more = [elem for elem in items if elem > pivot]
    return quicksort(less) + [pivot] + quicksort(more)


def time_algorithm(algorithm: Callable, list_size: int) -> float:
    test_data = random.sample(range(1, list_size * 10), list_size)
    timer = timeit.Timer(lambda: algorithm(test_data))
    return timer.timeit(1)



def main():
    sizes = [n for n in range(100, 10_000, 100)]
    algorithms = [('Quicksort', quicksort),
                  ('Selection Sort', sort_with_selection_sort)]

    extrapolate_size = 10**10 # This is the size you want to extrapolate for
    # No one would ever be silly enough to try and do an actual selection sort 
    # on a list this big! 

    plt.figure(figsize=(10, 5))

    for algo_name, algo in algorithms:
        times = [time_algorithm(algo, size) for size in sizes]
        plt.plot(sizes, times, 'o-', label=algo_name)

        if algo_name == 'Selection Sort':
            # Quadratic fit for Selection Sort
            coefficients = np.polyfit(sizes, times, 2)
            estimated_time = coefficients[0] * extrapolate_size**2 + coefficients[1] * extrapolate_size + coefficients[2]
        elif algo_name == 'Quicksort':
            # Log-linear fit for Quicksort
            log_sizes = np.log(sizes)
            coefficients = np.polyfit(sizes * log_sizes, times, 1)
            estimated_time = coefficients[0] * extrapolate_size * np.log(extrapolate_size) + coefficients[1]

        print(f"Estimated {algo_name} time for n={extrapolate_size}: {estimated_time:.4f} seconds")

    plt.title('Sorting Algorithms Execution Time vs. List Size')
    plt.xlabel('List Size')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.xscale('linear')
    plt.show()


if __name__ == '__main__':
    main()



# Example, how you could test sorting. 
# class TestMySort(unittest.TestCase):
#     def setUp(self) -> None:
#         self.test_list = random.sample(range(12_000), 10_000)
#
#     def test_selection_sort(self):
#         self.assertListEqual(sort_with_selection_sort(self.test_list),
#                              sorted(self.test_list))
#
#
