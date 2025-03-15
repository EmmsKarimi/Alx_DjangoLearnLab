from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library, Book

# Function-Based View (FBV) - List all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View (CBV) - Display details for a specific library
class LibraryDetailView(DetailView):
    model = Library  # ✅ Ensure Library is used here
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
