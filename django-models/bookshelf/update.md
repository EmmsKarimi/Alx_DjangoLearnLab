# Updating a Book Instance

```python
from bookshelf.models import Book

# Retrieving the book instance we created earlier
book = Book.objects.get(title="1984")

# Updating the title
book.title = "Nineteen Eighty-Four"
book.save()

# Displaying the updated book details
print(f"Updated Title: {book.title}, Author: {book.author}, Publication Year: {book.publication_year}")
