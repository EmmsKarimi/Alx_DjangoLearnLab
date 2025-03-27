from django.db import models

"""Represents an author who has written books."""
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

"""Represents a book with a title, publication year, and an associated author."""
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
