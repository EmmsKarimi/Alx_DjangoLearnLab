from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import profile, add_comment, edit_comment, delete_comment

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', profile, name='profile'),

    # Comment functionality
    path('posts/<int:post_id>/comments/new/', add_comment, name='add_comment'),
    path('comments/<int:comment_id>/edit/', edit_comment, name='edit_comment'),
    path('comments/<int:comment_id>/delete/', delete_comment, name='delete_comment'),
]
