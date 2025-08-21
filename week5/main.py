import random
from src.helpers import make_unique_random_list, time_call, make_random_graph
from src.binary_search import *
from src.linear_search import *
from src.breadth_first_search import *

def run_experiment_1(seed=42, n=10_000, trials=10000, low=1, high=12_000):
    """
    Timing experiment to compares different search strategies.

    The function generates a dataset of unique random integers, then times
    how long it takes to locate randomly chosen "needle" values using:
      - Linear search on an unsorted list
      - Linear search on a sorted list
      - Binary search on an unsorted list
      - Binary search on a sorted list

    Args:
        seed (int): Random seed for reproducibility.
        n (int): Size of the dataset (number of items).
        trials (int): Number of search queries to time.
        low (int): Minimum possible value in the dataset.
        high (int): Maximum possible value in the dataset.

    Returns:
        None. Prints average search times (in ms) for each method.
    """
    random.seed(seed)

    # Create unsorted data set of unique items
    data_unsorted = make_unique_random_list(n, low, high)

    # Needles: mix of present and potentially absent
    needles_present = random.sample(data_unsorted, trials // 2)
    needles_random  = random.sample(range(low, high + 1), trials - len(needles_present))
    needles = needles_present + needles_random
    random.shuffle(needles)

    # sort it
    data_sorted = sorted(data_unsorted)

    # Linear search on UNSORTED
    avg_time_linear_unsorted = sum(
        time_call(lambda: linear_search(x, data_unsorted)) for x in needles
    ) / trials

    # Linear search on SORTED
    avg_time_linear_sorted = sum(
        time_call(lambda: linear_search(x, data_sorted)) for x in needles
    ) / trials

    # Binary search on UNSORTED


    # Binary search on SORTED
 

    print(f"Linear Search(unsorted) ms: {avg_time_linear_unsorted}")
    print(f"Linear Search(sorted)   ms: {avg_time_linear_sorted}")
    # print(f"Binary Search(unsorted) ms: {avg_time_binary_unsorted}")
    # print(f"Binary Search(sorted)   ms: {avg_time_binary_sorted}")


def run_experiment_2(n_nodes: int = 10_000, avg_neighbours: int = 6,trials: int = 10000, seed: int = 123):
    """
    Time BFS vs DFS (iterative) over many random start/goal pairs on a graph.

    Args:
        n_nodes (int): number of nodes in the graph.
        avg_degree (int): approximate outgoing edges per node (controls density).
        trials (int): number of (start, goal) search queries to time.
        seed (int): random seed for reproducibility.

    Returns:
        dict: {
            'BFS (avg ms)': float,
            'DFS (avg ms)': float
        }
    """
    rng = random.Random(seed)
    graph = make_random_graph(n=n_nodes, avg_degree=avg_neighbours, seed=seed)

    # random start/goal pairs
  

    # create a starting time for each algotihm


if __name__ == "__main__":
    run_experiment_1()

    graph_results = run_experiment_2()

    print("\nAverage time (ms) over 10000 Graph searches (BFS vs DFS)")
    for k, v in graph_results.items():
        print(f"{k}: {v:.6f}")