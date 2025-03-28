from django.db import models
import datetime

class Author(models.Model):
    """
    Model to represent an Author.
    
    Fields:
    - name: Stores the author's name.
    - created_at: Timestamp for when the author was added.
    """
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} (Added on {self.created_at.date()})"

class Book(models.Model):
    """
    Model to represent a Book.
    
    Fields:
    - title: Stores the book title.
    - publication_year: Stores the year of publication (validated).
    - author: Foreign key linking the book to an author.
    - created_at: Timestamp for when the book was added.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        """
        Validate that publication_year is not in the future.
        """
        current_year = datetime.date.today().year
        if self.publication_year > current_year:
            raise ValueError("Publication year cannot be in the future.")

    def __str__(self):
        return f"{self.title} ({self.publication_year}) by {self.author.name}"
