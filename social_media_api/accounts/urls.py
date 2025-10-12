from django.urls import path
from .views import RegisterView, LoginView, ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
     path('follow/<int:user_id>/', views.FollowToggleAPIView.as_view(), name='follow-toggle'),
    path('following/', views.FollowingListView.as_view(), name='following-list'),
    path('followers/', views.FollowersListView.as_view(), name='followers-list'),
      path('feed/', views.FeedView.as_view(), name='feed'),
]
