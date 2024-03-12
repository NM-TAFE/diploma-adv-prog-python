import random


def create_pearson_table(seed=42):
    random.seed(seed)
    pearson = list(range(256))
    random.shuffle(pearson)
    return pearson


DEFAULT = tuple(create_pearson_table())


def pearson_hash(data,
                 sub_table=DEFAULT):
    if isinstance(data, str):
        data = bytes(data, encoding='utf8')
    hash_ = 0
    for byte in data:
        hash_ = sub_table[byte ^ hash_]
    return hash_
