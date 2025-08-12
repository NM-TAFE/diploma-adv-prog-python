from math import sqrt  # Import square root function for prime number checking
from hash_entry import HashEntry  # Import HashEntry class for storing key-value pairs

class HashTable:
    """"
    Implementation of double hashing  - this different to linear probling as is 
    avoids clustering of values with the same key which in turn reduces long runs of searches of identical keys
    """
    def __init__(self, ts):
        # Constructor to initialise the hash table with size and empty slots
        self.__size = 0 
        self.__TABLE_SIZE = ts  
        self.__table = [None] * ts 
        self.__prime_size = self.__get_prime()  # Find a prime number < table size for hash2

    def insert(self, key, value):
        """Insert a key-value pair into the hash table
        """
        if self.__size == self.__TABLE_SIZE:
            # If table is full, raise an error
            raise RuntimeError("Table full!")

        hash1 = self.__hash1(key)  # Compute first hash (index based on key)
        hash2 = self.__hash2(hash1)  # Compute second hash for double hashing step size

        # Probe until an empty slot is found using double hashing
        while self.__table[hash1] is not None:
            hash1 = (hash1 + hash2) % self.__TABLE_SIZE  # Linear jump using hash2

        # Is this just not a linked list???
        self.__table[hash1] = HashEntry(key, value)  # Insert new entry at found index
        self.__size += 1 

    def remove(self, key):
        """Remove a key-value pair from the hash table
        """
        if self.__size == 0:
            # If table is empty, nothing to remove
            return

        hash1 = self.__hash1(key)  # Compute index using first hash
        hash2 = self.__hash2(hash1)  # Compute step size using second hash

        # Probe until we find the key or hit an empty slot
        while self.__table[hash1] is not None and self.__table[hash1].key != key:
            hash1 = (hash1 + hash2) % self.__TABLE_SIZE 

        self.__table[hash1] = None  # Remove the item by setting to None
        self.__size -= 1

    def __get_prime(self):
        """Find the largest prime number less than the table size
        Used for the second hash function (hash2)
        """
        for i in range(self.__TABLE_SIZE - 1, 0, -1):
            fact = False  # Assume i is prime
            for j in range(2, int(sqrt(i)) + 1):  # Check divisibility from 2 to √i
                if i % j == 0:
                    fact = True  # i is not prime
                    break
            if not fact:
                return i  # Return the first prime found

        return 3 

    def __hash1(self, s):
        """
        Primary hash function for a key
        """
        hash_val = hash(s) % self.__TABLE_SIZE  # Use Python's built-in hash and the modulus of the table size
        return hash_val if hash_val >= 0 else hash_val + self.__TABLE_SIZE  # Ensure non-negative

    def __hash2(self, h):
        """
        Secondary hash function based on original hash value
        Ensures a step size for double hashing
        """
        return self.__prime_size - h % self.__prime_size  # Offset to avoid clustering

    def __str__(self):
        # String representation: print all key-value pairs in the table
        s = ""
        for i in range(self.__TABLE_SIZE):
            if self.__table[i] is not None:
                print(self.__table[i].key, self.__table[i].value)
        return s

