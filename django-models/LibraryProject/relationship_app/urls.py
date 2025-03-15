from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # ✅ Ensure this is included

urlpatterns = [
    # Book & Library Views
    path('books/', views.list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # Class-based view

    # Authentication URLs
    path('register/', views.register_view, name='register'),  # User Registration
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # User Login
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # User Logout

    # Role-Based Access URLs
    path('admin-dashboard/', views.admin_view, name='admin_view'),  # Admin Dashboard
    path('librarian-dashboard/', views.librarian_view, name='librarian_view'),  # Librarian Dashboard
    path('member-dashboard/', views.member_view, name='member_view'),  # Member Dashboard
]
