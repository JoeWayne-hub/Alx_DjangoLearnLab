from django.contrib import admin
from .models import Book

# bookshelf/admin.py
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Display fields in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add search bar to search by title or author
    search_fields = ('title', 'author')
    
    # Add filters by publication year
    list_filter = ('publication_year',)
    
    # Add ordering by publication year (descending)
    ordering = ('-publication_year',)

# Register the model with the admin interface
admin.site.register(Book, BookAdmin)

