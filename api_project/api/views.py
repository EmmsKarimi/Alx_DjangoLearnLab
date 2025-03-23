from rest_framework.generics import ListAPIView  # Ensure ListAPIView is imported
from .models import Book
from .serializers import BookSerializer

class BookList(ListAPIView):  # Ensure the class extends ListAPIView
    queryset = Book.objects.all()
    serializer_class = BookSerializer
