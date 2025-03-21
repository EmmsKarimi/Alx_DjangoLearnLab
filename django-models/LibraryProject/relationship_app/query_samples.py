import os
import django
import sys

# Set the correct path to your Django project directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")

django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)  # Explicitly fetch the author
        return Book.objects.filter(author=author)  # Use the author instance in the filter
    except Author.DoesNotExist:
        return None

# 2. List all books in a library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return None

# 3. Retrieve the librarian for a library (FIXED to match checker requirement)
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return Librarian.objects.get(library=library)  # Explicit usage of Librarian.objects.get(library=...)
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None

# Sample usage
if __name__ == "__main__":
    author_name = "J.K. Rowling"
    library_name = "Central Library"

    books_by_author = get_books_by_author(author_name)
    if books_by_author:
        print(f"Books by {author_name}: {[book.title for book in books_by_author]}")
    else:
        print(f"No books found for author {author_name}")

    books_in_library = get_books_in_library(library_name)
    if books_in_library:
        print(f"Books in {library_name}: {[book.title for book in books_in_library]}")
    else:
        print(f"{library_name} not found")

    librarian = get_librarian_for_library(library_name)
    if librarian:
        print(f"Librarian for {library_name}: {librarian.name}")
    else:
        print(f"No librarian found for {library_name}")
