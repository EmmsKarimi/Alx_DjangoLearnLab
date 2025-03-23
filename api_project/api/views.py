from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated  # Import permissions
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):  
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access

class BookViewSet(viewsets.ModelViewSet):  
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Require authentication for all CRUD actions
