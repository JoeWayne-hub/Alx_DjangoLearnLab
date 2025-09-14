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

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'date_of_birth', 'profile_photo', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
