# Searching Algorithms — Kaggle-backed Exercise
# Dataset: NYC 311 Service Requests (2010–Present)
# Source: Kaggle (contains a numeric 'Unique Key' per record)
# https://www.kaggle.com/datasets/taylorsamarel/311-service-requests-nyc
# Slides referenced by title keywords from 'Python-Searching_v2.pptx'.

import pandas as pd
import random
from bisect import bisect_left
from src.helpers import *
from src.binary_search import *
from src.linear_search import *


# ---------------------------------------------------------------------------
# Load dataset from Kaggle CSV
CSV_PATH = "./data/311_service_requests.csv"  # update this path as needed
ID_COLUMN = "Unique Key"

df = pd.read_csv(CSV_PATH, usecols=[ID_COLUMN])

# Convert to plain Python list for algorithm-only timing
all_request_ids = df[ID_COLUMN].astype("int64").tolist()

# Safe demo sample
TARGET_SAMPLE_SIZE = 50_000
sample_size = min(TARGET_SAMPLE_SIZE, len(all_request_ids))
if sample_size < TARGET_SAMPLE_SIZE:
    print(f"[info] Dataset has only {len(all_request_ids):,} rows; sampling {sample_size:,}.")
request_ids_unsorted = random.sample(all_request_ids, k=sample_size)

print(f"Loaded {len(request_ids_unsorted):,} request IDs from Kaggle dataset.")

def set_lookup(target_id, id_set):
    """Return True if target_id is in id_set, else False."""
    return target_id in id_set

def dict_lookup(target_id, id_dict):
    """Return True if target_id is in id_dict (dict keys), else None."""
    return id_dict.get(target_id)

# ---------------------------------------------------------------------------
# Build test needles: half guaranteed present, half absent
random.seed(42)
NUM_TRIALS = 10000
dataset_size = len(request_ids_unsorted)

present_needles = random.sample(request_ids_unsorted, k=min(NUM_TRIALS // 2, dataset_size))
max_existing_id = max(request_ids_unsorted)
absent_needles = [max_existing_id + 1 + i for i in range(NUM_TRIALS - len(present_needles))]

test_needles = present_needles + absent_needles
random.shuffle(test_needles)

# build the random structures for the test
request_ids_sorted = sorted(request_ids_unsorted)
request_id_set = set(request_ids_unsorted)
dict_sample_size = min(200_000, dataset_size)
request_id_dict = {req_id: True for req_id in random.sample(request_ids_unsorted, k=dict_sample_size)}

# Benchmark suite
print("\nBenchmarking …")

avg_time_linear_unsorted = sum(
    time_call(lambda target=needle: linear_search(target, request_ids_unsorted))
    for needle in test_needles
) / len(test_needles)

avg_time_linear_sorted = sum(
    time_call(lambda target=needle: linear_search(target, request_ids_sorted))
    for needle in test_needles
) / len(test_needles)

avg_time_binary_sorted = sum(
    time_call(lambda target=needle: binary_search_iter(target, request_ids_sorted))
    for needle in test_needles
) / len(test_needles)

avg_time_binary_sorted = sum(
    time_call(lambda target=needle: binary_search_iter(target, request_ids_sorted))
    for needle in test_needles
) / len(test_needles)

avg_time_set_lookup = sum(
    time_call(lambda target=needle: set_lookup(target, request_id_set))
    for needle in test_needles
) / len(test_needles)

avg_time_dict_lookup = sum(
    time_call(lambda target=needle: dict_lookup(target, request_id_dict))
    for needle in test_needles
) / len(test_needles)

# ---------------------------------------------------------------------------
# Results
print(f"Average over {len(test_needles)} PANDA trials (ms):")
print(f"  Linear (unsorted): {avg_time_linear_unsorted:.6f} ms   [Slide: Linear search]")
print(f"  Linear (sorted):   {avg_time_linear_sorted:.6f} ms     [Slide: Linear search]")
print(f"  Binary (sorted):   {avg_time_binary_sorted:.6f} ms     [Slide: Binary search]")
print(f"  Set lookup:        {avg_time_set_lookup:.6f} ms        [Hash/set comparison]")
print(f"  Dict lookup:       {avg_time_dict_lookup:.6f} ms       [Hash/dict comparison]")