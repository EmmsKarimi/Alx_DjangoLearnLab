from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# Function-Based View (FBV) - List all books
def list_books(request):
    books = Book.objects.all()  # Query all books
    return render(request, 'relationship_app/list_books.html', {'books': books})  # Updated template path

# Class-Based View (CBV) - Display details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Updated template path
    context_object_name = 'library'
