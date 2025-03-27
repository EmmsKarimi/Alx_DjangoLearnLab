from rest_framework import serializers
from .models import Author, Book
import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    Converts Book model instances to JSON and validates input data.
    """
    class Meta:
        model = Book
        fields = '__all__'  # Includes all fields (title, publication_year, author)

    def validate_publication_year(self, value):
        """
        Custom validation to ensure publication year is not in the future.
        """
        if value > datetime.datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value  # Returns the valid year


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    Includes all books written by the author as nested data.
    """
    books = BookSerializer(many=True, read_only=True)  
    # Serializes related books as a nested list, but only for read operations.

    class Meta:
        model = Author
        fields = ['name', 'books']  # Returns the author's name and their books
