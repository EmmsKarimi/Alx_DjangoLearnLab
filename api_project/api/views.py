from rest_framework import generics, viewsets  # Import generics and viewsets
from .models import Book
from .serializers import BookSerializer

# ListAPIView for retrieving all books
class BookList(generics.ListAPIView):  
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# ViewSet for full CRUD operations (Create, Read, Update, Delete)
class BookViewSet(viewsets.ModelViewSet):  
    queryset = Book.objects.all()
    serializer_class = BookSerializer
