# posts/urls.py
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from django.urls import path, include
from .views import FeedView


router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view(), name='feed'),
    path('posts/<int:pk>/like/', LikeCreateView.as_view(), name='post-like'),
    path('posts/<int:pk>/unlike/', LikeRemoveView.as_view(), name='post-unlike'),
]