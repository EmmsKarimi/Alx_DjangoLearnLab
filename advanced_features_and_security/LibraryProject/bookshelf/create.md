# Creating a Book Instance

```python
from bookshelf.models import Book

# Creating a book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Checking if the book was created successfully
print(book)
