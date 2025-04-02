from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from . import views

# Create a router and register viewsets
router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    # Include the routes from the router for Post and Comment
    path('', include(router.urls)),
    
    # Add the route for the user feed
    path('feed/', views.user_feed, name='user_feed'),
]
