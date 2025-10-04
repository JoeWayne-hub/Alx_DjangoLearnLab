from django.contrib import admin
from .models import Profile
from .models import Post, Comment

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_role')  
    admin.site.register(Post)
    admin.site.register(Comment)