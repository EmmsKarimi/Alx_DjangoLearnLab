# Deleting a Book Instance

```python
from bookshelf.models import Book

# Retrieving the book instance we created earlier
book = Book.objects.get(title="Nineteen Eighty-Four")

# Deleting the book instance
book.delete()

# Confirming the deletion by checking if any books exist
books = Book.objects.all()
print(f"Remaining books in the database: {books.count()}")
