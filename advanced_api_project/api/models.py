from django.db import models

class Author(models.Model):
    """
    Represents an author who writes books.
    Each author can have multiple books (One-to-Many relationship).
    """
    name = models.CharField(max_length=255)  # Stores the author's name

    def __str__(self):
        return self.name  # Returns the author's name when printed


class Book(models.Model):
    """
    Represents a book written by an author.
    Each book is linked to a single author.
    """
    title = models.CharField(max_length=255)  # Stores the book title
    publication_year = models.IntegerField()  # Stores the publication year of the book
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='books'
    )  # Links the book to an author, deleting an author removes their books

    def __str__(self):
        return self.title  # Returns the book title when printed
