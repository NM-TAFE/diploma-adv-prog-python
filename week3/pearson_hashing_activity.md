# Build a Multi-Byte Pearson Hash Function in Python

## Description

Write a **multi-byte Pearson hashing function** that converts a string into a sequence of `n` hash bytes.

Using the example provided each byte will be computed using:

- A permutation table
- A hash seed based on the round number
- A dictionary of values created from the permutation table
- {index: value for index, value in enumerate(PERMUTATION_TABLE)}
- Bitwise XOR and modular operations
- Convert characters to ASCII values
- Use XOR in Python (exclusive or)
- Make sure all values stay within 0–255 using a modulus
- Loop through `input_str[1:]` inside the hashing loop - why do we do this

## Output Example

For input `"hello"` and `length = 4`, your result should look something like:

```python
[142, 115, 15, 248]
```

(Your exact numbers may vary if you change the seed or permutation table.)

1. Modify the function to return a **single 32-bit integer** instead of a list
2. Convert the hash result into a **hex string**
3. Try different seeds and analyse how the output changes
4. Make the permutation table a parameter — try randomising it on each run
