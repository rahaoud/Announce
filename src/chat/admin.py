from django.contrib import admin

# Register your models here.

from .models import Thread, Message
# from users.models import UserProfile
# Register your models here.

admin.site.register(Thread)
admin.site.register(Message)
# admin.site.register(UserProfile)
