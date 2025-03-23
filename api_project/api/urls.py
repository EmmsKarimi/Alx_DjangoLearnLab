from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token  # Import token view
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Create a router and register the BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to BookList view
    path('', include(router.urls)),  # Includes all ViewSet routes
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Token authentication endpoint
]
