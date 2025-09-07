from django.urls import path
from .views import list_books, LibraryDetailView  # ✅ explicit import required

urlpatterns = [
    path('books/', list_books, name='list_books'),  # function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # class-based view
]
from django.urls import path
from .views import register
from django.contrib.auth.views import LoginView, LogoutView  # Import built-in views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # Login view
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # Logout view
    path('register/', register, name='register'),  # Registration view (custom)
]
