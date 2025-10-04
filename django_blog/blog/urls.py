from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import PostByTagListView

urlpatterns = [
    # Registration
    path('register/', views.register_view, name='register'),
    # Login / logout - using Django's built-in views and template names
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logged_out.html'), name='logout'),
    # Profile view / edit
    path('profile/', views.profile_view, name='profile'),
    path("", views.PostListView.as_view(), name="post-list"),
    path("post/new/", views.PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", views.PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post-delete"),
     path('post/<int:post_pk>/comments/new/', views.comment_create, name='comment-create'),
    path('comment/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
    path('post/<int:post_pk>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
    path('tags/<str:tag_name>/', views.TagPostListView.as_view(), name='tag-posts'),
    path('search/', views.SearchResultsView.as_view(), name='search-results'), 
    path('search/', views.SearchResultsView.as_view(), name='search-results'),  
    path('tags/<slug:tag_slug>/', views.TagPostListView.as_view(), name='tag-posts'),  
    path('tags/<str:tag_name>/',PostByTagListView.as_view(), name='posts_by_tag'),  
]


