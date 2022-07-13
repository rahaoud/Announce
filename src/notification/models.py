
# Create your models here.

from django.db import models
import uuid

from announce.models import Announce
from users.models import MyUser
# from discussion.models import Discussion
# from feed.models import Mumble


class Notification(models.Model):
    CHOICES = (
        ('article', 'article'),
        ('mumble', 'mumble'),
        ('discussion', 'discussion'),
        ('follow', 'follow'),
    )

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    to_user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True, related_name='notifications')
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)
    content = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    notification_type = models.CharField(max_length=20, choices=CHOICES)
    article = models.ForeignKey(Announce, on_delete=models.CASCADE, null=True, blank=True)
    # mumble = models.ForeignKey(Mumble, on_delete=models.CASCADE, null=True, blank=True)
    # discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, null=True, blank=True)
    followed_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True, related_name='followed_by')

    def __str__(self):
        return self.content
