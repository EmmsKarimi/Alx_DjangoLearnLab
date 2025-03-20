from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

@login_required
def book_list(request):
    """View to display a list of books."""
    return render(request, "bookshelf/book_list.html")

@permission_required("bookshelf.can_create", raise_exception=True)
def create_book(request):
    """View to create a new book (restricted by permission)."""
    return render(request, "bookshelf/create_book.html")

@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_book(request):
    """View to delete a book (restricted by permission)."""
    return render(request, "bookshelf/delete_book.html")
