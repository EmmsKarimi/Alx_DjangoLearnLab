from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # Ensure this is included

urlpatterns = [
    path('books/', views.list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # Class-based view

    # Authentication URLs
    path('register/', views.register_view, name='register'),  # User Registration
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # User Login
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # User Logout
]
