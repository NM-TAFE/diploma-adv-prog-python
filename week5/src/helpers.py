import random
from time import perf_counter_ns


# ---------- Data generation ----------
def make_unique_random_list(n=10_000, low=1, high=12_000):
    """ returns unsorted order"""
    arr = random.sample(range(low, high + 1), k=n)
    random.shuffle(arr) 
    return arr


def make_random_graph(n: int = 20_000, avg_degree: int = 4, seed: int = 42):
    """
    Create a directed graph as an adjacency list with ~avg_degree neighbors per node.
    """
    random_instance = random.Random(seed)
    nodes = list(range(n))
    graph = {adj_members: [] for adj_members in nodes}
    # For each node, sample up to 'avg_degree' distinct neighbors
    for this_node in nodes:
        pool = nodes[:this_node] + nodes[this_node+1:] 
        k = min(avg_degree, len(pool))
        neighbors = random_instance.sample(pool, k=k)
        graph[this_node] = neighbors
    return graph


def convert_to_ms(ns): 
    """float milliseconds"""   
    return ns / 1_000_000.0


def time_call(algorithm_called, repeats=1):
    total = 0
    for _ in range(repeats):
        time_0 = perf_counter_ns()
        # run the function
        algorithm_called()
        time_1 = perf_counter_ns()
        total += (time_1 - time_0)
    return convert_to_ms(total / repeats)
    
