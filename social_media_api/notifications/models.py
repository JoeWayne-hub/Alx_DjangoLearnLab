from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

User = settings.AUTH_USER_MODEL

class Notification(models.Model):
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='actor_notifications')
    verb = models.CharField(max_length=255)  # e.g., "liked", "commented", "followed"
    # Generic target (post/comment/other)
    target_ct = models.ForeignKey(ContentType, null=True, blank=True, on_delete=models.SET_NULL)
    target_id = models.PositiveIntegerField(null=True, blank=True)
    target = GenericForeignKey('target_ct', 'target_id')

    unread = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"Notification: {self.actor} {self.verb} -> {self.recipient}"
