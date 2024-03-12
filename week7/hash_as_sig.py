from custom_hashing import pearson_hash

with open('README.md') as f:
    content = f.read()
SIZE = 10
contents = [None] * SIZE
h = pearson_hash(content)
index = h % SIZE
contents[index] = content
content1 = "Hello, World"
h1 = pearson_hash(content1)
index1 = h1 % SIZE
print(contents[index1])
print(contents)
