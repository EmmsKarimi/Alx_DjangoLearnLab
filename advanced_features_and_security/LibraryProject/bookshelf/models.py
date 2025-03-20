from django.db import models

class Book(models.Model):
    """Represents a book in the library system."""
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField(null=True, blank=True)

    class Meta:
        permissions = [
            ("can_create", "Can create books"),
            ("can_delete", "Can delete books"),
        ]

    def __str__(self):
        return self.title
