from rest_framework import serializers
from .models import Author, Book
import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    
    - Serializes all fields.
    - Adds validation to ensure the publication year is not in the future.
    - Accepts author ID for easier book creation.
    """

    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), source='author.id')

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """
        Ensure the publication year is not in the future.
        """
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    
    - Includes all author fields.
    - Uses a nested BookSerializer to serialize related books.
    - Allows book creation within the author serializer.
    """

    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
