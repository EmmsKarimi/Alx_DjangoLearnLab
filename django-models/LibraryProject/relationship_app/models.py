from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Define role choices
ROLE_CHOICES = [
    ('Admin', 'Admin'),
    ('Librarian', 'Librarian'),
    ('Member', 'Member'),
]

# Existing Models
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")  # Added related_name

    class Meta:
        permissions = [
            ("can_add_book", "Can add a book"),  # Ensured wording matches views.py
            ("can_change_book", "Can edit a book"),
            ("can_delete_book", "Can delete a book"),
        ]

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name="libraries")  # Added related_name

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=255)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name="librarian")  # Added related_name

    def __str__(self):
        return self.name

# New Model: UserProfile for Role-Based Access Control
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")  # Added related_name
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"

# Signal to automatically create and save UserProfile when a new User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.profile.save()
