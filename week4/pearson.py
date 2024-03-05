import random

def create_pearson():
    random.seed(42)
    pearson = list(range(256))
    random.shuffle(pearson)
    return pearson

def pearson_hash(data, sub_table):
    if isinstance(data, str):
        data = bytes(data, encoding='utf8')
    hash = 0
    for byte in data:
        hash = sub_table[byte ^ hash]
    return hash

p = create_pearson()
# p = list(range(256))
print(pearson_hash("b", p))

