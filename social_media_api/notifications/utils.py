from django.contrib.contenttypes.models import ContentType
from .models import Notification

def create_notification(actor, recipient, verb, target):
    if actor != recipient:  # Don't notify users of their own actions
        Notification.objects.create(
            actor=actor,
            recipient=recipient,
            verb=verb,
            target_content_type=ContentType.objects.get_for_model(target),
            target_object_id=target.id,
        )
