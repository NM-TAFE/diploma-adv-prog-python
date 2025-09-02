import pprint
# Special methods: See https://realpython.com/python-repr-vs-str/

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    # Human-readable string
    def __str__(self):
        return f"'STRING BOOK:{self.title}' by {self.author}"
    
    # Detailed string for debugging
    def __repr__(self):
        return f" REPR BOOK: Book(title={self.title!r}, author={self.author!r}, year={self.year!r})" 

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added {book}")  # Uses __str__ for a humand readable message
    
    def __str__(self):
        return f"Library with {len(self.books)} Australian books"

    def __repr__(self):
        return f"Library(books={self.books!r})"  # Uses __repr__ of Book objects

# Creating 3 books instances
book1 = Book("My Brilliant Career", "Miles Franklin", 1901)
book2 = Book("Cloudstreet", "Tim Winton", 1991)
book3 = Book("The Secret River", "Kate Grenville", 2005)

# Creating a library and adding books
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Printing the library (calls __str__)
print(f"Print Library using __str__: {library}")
# Inspecting the library (calls __repr__)
print(f"Print Library using __repr__: {repr(library)}")
pprint.pprint(f"PPrint Library using __repr__: {repr(library)}")

# Inspecting the book (calls __repr__)
print(f"Print Book using __repr__: {repr(book1)}")
pprint.pprint(f"PPrint Book using __repr__: {repr(book1)}")
