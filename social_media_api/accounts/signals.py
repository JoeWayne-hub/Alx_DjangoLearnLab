from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from notifications.models import Notification

User = get_user_model()

@receiver(m2m_changed, sender=User.following.through)
def create_follow_notification(sender, instance, action, pk_set, **kwargs):
    # instance is the user whose following set changed (i.e., instance.following.add(target))
    if action == "post_add":
        for target_pk in pk_set:
            try:
                actor = instance
                recipient = User.objects.get(pk=target_pk)
                if actor != recipient:
                    Notification.objects.create(
                        recipient=recipient,
                        actor=actor,
                        verb="followed you",
                        target_ct=None,
                        target_id=None
                    )
            except User.DoesNotExist:
                continue
