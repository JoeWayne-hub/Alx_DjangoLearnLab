from django.shortcuts import render
from django.views.generic.detail import DetailView  # ✅ must be this exact import

from .models import Book
from .models import Author
from .models import Librarian
from .models import Library  # ✅ explicit import required

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display a specific library's details, including its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
