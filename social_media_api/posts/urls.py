from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, user_feed

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('feed/', user_feed, name='user_feed'),  # Feed view
    path('', include(router.urls)),  # Registers Post and Comment viewsets
]
