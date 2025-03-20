# Retrieving a Book Instance

```python
from bookshelf.models import Book

# Retrieving the book instance we created earlier
book = Book.objects.get(title="1984")

# Displaying all attributes of the retrieved book
print(f"Title: {book.title}, Author: {book.author}, Publication Year: {book.publication_year}")
