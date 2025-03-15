from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),  # URL for function-based view (FBV)
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # URL for class-based view (CBV)
]
