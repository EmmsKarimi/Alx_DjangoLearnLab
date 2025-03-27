"""
Models for the API:
- Author: Represents a book author with a name field.
- Book: Represents a book written by an author. It includes:
    - title: The title of the book.
    - publication_year: The year the book was published.
    - author: A foreign key linking the book to an Author, establishing a one-to-many relationship.
"""

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
