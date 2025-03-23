from django.urls import path, include
from rest_framework.routers import DefaultRouter  # Import DefaultRouter
from .views import BookList, BookViewSet  # Import BookList and BookViewSet

# Create a router and register our ViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to BookList view
    path('', include(router.urls)),  # Includes all ViewSet routes
]
