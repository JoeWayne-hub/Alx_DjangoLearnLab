from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Registration
    path('register/', views.register_view, name='register'),
    # Login / logout - using Django's built-in views and template names
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logged_out.html'), name='logout'),
    # Profile view / edit
    path('profile/', views.profile_view, name='profile'),
]
