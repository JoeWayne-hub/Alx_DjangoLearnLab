from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'actor', 'verb', 'unread', 'timestamp')
    list_filter = ('unread', 'timestamp')
