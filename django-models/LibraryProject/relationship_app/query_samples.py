import django
from django.conf import settings
from relationship_app.models import Author, Book, Library, Librarian

# Setup Django environment
settings.configure()
django.setup()

# Sample Queries

# 1. Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books

# 2. List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

# 3. Retrieve the librarian for a library (corrected query)
def librarian_of_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)  # Corrected line to query Librarian
    return librarian

if __name__ == "__main__":
    # Example Usage
    # Query all books by an author
    print(books_by_author("J.K. Rowling"))
    
    # List all books in a library
    print(books_in_library("City Library"))
    
    # Retrieve the librarian for a library
    print(librarian_of_library("City Library"))
