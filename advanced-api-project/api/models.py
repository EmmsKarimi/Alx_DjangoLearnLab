from django.db import models

class Author(models.Model):
    """
    Model to represent an Author.
    
    Fields:
    - name: Stores the author's name.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Model to represent a Book.
    
    Fields:
    - title: Stores the book title.
    - publication_year: Stores the year of publication.
    - author: Foreign key linking the book to an author.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.title
