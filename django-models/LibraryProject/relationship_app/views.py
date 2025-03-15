from django.shortcuts import render  # ✅ Ensure this import is present
from django.views.generic import DetailView  # ✅ Import Django's class-based view
from .models import Book, Library  # ✅ Ensure both models are explicitly imported

# Function-Based View (FBV) - List all books
def list_books(request):
    books = Book.objects.all()  # Query all books
    return render(request, 'relationship_app/list_books.html', {'books': books})  # ✅ Ensure correct template path

# Class-Based View (CBV) - Display details for a specific library
class LibraryDetailView(DetailView):
    model = Library  # ✅ Ensure Library model is correctly referenced
    template_name = 'relationship_app/library_detail.html'  # ✅ Ensure correct template path
    context_object_name = 'library'  # ✅ Ensure correct context name
