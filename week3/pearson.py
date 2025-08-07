import random

PERMUTATION_TABLE = list(range(256))

random.seed(5)
random.shuffle(PERMUTATION_TABLE)

def pearson_hash(input_string: str) -> int:
    # store the result
    # take string
    # use the ascii and use a modulus (256) will be the index of in the permutation
    hash_value = 0

    for char in input_string:
        xor_value = hash_value ^ ord(char)
        hash_value = PERMUTATION_TABLE[xor_value]

    return hash_value


print(f"Hash of 'hello': {pearson_hash('hello')}")