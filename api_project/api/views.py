from rest_framework import generics  # Import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):  # Ensure it extends ListAPIView
    queryset = Book.objects.all()
    serializer_class = BookSerializer
