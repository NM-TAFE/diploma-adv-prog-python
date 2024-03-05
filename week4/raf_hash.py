from typing import Any

ARRAY_SIZE: int = 42

def raf_hash(data: str, size: int = ARRAY_SIZE) -> int:
    return sum(ord(c) for c in data) % size


array = [None] * ARRAY_SIZE
num, name = '500', 'Raf'
num2, name2 = '300', 'Jo'
array[raf_hash(num)] = name
array[raf_hash(num2)] = name2
print(array[raf_hash(num)], f'{raf_hash(num) = }')
print(array[raf_hash(num2)], f'{raf_hash(num2) = }')
print(array)
