from hash_table import HashTable

if __name__ == '__main__':
    # Create a hash table with 10 slots
    hash_table = HashTable(10)
    # hash_table.__hash2('John') 
    hash_table.insert("John", "John Doe")  # Insert key-value pair
    hash_table.insert("Jane", "Jane Doe")  # Insert another key-value pair

    print(hash_table)  # Print the contents of the hash table