from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library

# Function-Based View (FBV) - List all books
def list_books(request):
    books = Book.objects.all()  # Query all books
    return render(request, 'list_books.html', {'books': books})

# Class-Based View (CBV) - Display details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
