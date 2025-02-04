class Array:
    def __init__(self, max_size):
        self.array = [None] * max_size
        self.index = -1
        self.max_size = max_size

    def insert(self, item, pos):
        if pos > self.index:
            raise IndexError("Index out of bounds")
        self.array[pos] = item

    def append(self, item):
        if self.index == self.max_size:
            self._resize()
        self.index += 1
        self.array[self.index] = item


    def get(self, pos):
        if pos > self.index:
            raise IndexError("Index out of bounds")
        return self.array[pos]
    def _resize(self):
        temp_array = (self.max_size * 2) * [None]
        temp_array[:self.max_size] = self.array
        self.array = temp_array
        self.max_size *= 2
