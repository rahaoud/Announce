from django.db import models

# Create your models here.
from users.models import MyUser


# from django.contrib.auth.models import User
# Create your models here.

# class UserProfile(models.Model):
#     user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
#     is_online = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.user.username


# thread class with two user foreignkeys
class Thread(models.Model):
    user1 = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='user1')
    user2 = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='user2')
    last_message = models.CharField(max_length=200, default="")


class Message(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='thread')
    sender = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='user')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender.email + ': ' + self.message
