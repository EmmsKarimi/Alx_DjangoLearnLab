from django.db import models

class Author(models.Model):
    """
    Represents an author with a name.
    An author can have multiple books (One-to-Many relationship).
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Represents a book with a title, publication year, and an associated author.
    The `author` field establishes a foreign key relationship with the Author model,
    meaning each book belongs to one author, but an author can have multiple books.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
