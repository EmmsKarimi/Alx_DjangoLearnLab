"""
Serializers for the API:
- BookSerializer: Serializes the Book model with all fields included.
    - Includes a validation method to ensure the publication year is not in the future.
- AuthorSerializer: Serializes the Author model.
    - Includes a nested BookSerializer to serialize the related books dynamically.
"""

from rest_framework import serializers
from .models import Author, Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """Ensure the publication year is not in the future."""
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested serializer

    class Meta:
        model = Author
        fields = ['name', 'books']
