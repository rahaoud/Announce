from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.


import uuid


# A topic tag is added to by the user so they can content on their feed with the
# related tags that
# They have selected
from deals.settings import BASE_DIR


class TopicTag(models.Model):
    name = models.CharField(primary_key=True, max_length=150, null=False, blank=False)

    def __str__(self):
        return self.name


# Skills are added by teh user to indicate topics they are proficient in
class SkillTag(models.Model):
    name = models.CharField(primary_key=True, max_length=150, null=False, blank=False)

    def __str__(self):
        return self.name


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Vous devez entrer votre addresse email')
        else:
            user = self.model(email=self.normalize_email(email))
            user.set_password(password)
            user.save()
            return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email=email, password=password)
        user.is_staff = True
        user.is_admin = True
        user.save()
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(blank=False, max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    objects = MyUserManager()
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class UserProfile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=200, null=True)
    thumbnail = models.ImageField(upload_to='profile', blank=True, null=True, default='default.png')
    bio = models.TextField(null=True)
    vote_ratio = models.IntegerField(blank=True, null=True, default=0)
    followers_count = models.IntegerField(blank=True, null=True, default=0)
    skills = models.ManyToManyField(SkillTag, related_name='personal_skills', blank=True)
    interests = models.ManyToManyField(TopicTag, related_name='topic_interests', blank=True)
    followers = models.ManyToManyField(MyUser, related_name='following', blank=True)
    email_verified = models.BooleanField(default=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    """
    profile = UserProfile.objects.first()
    profile.followers.all() -> All users following this profile
    user.following.all() -> All user profiles I follow
    """
    thumbnail_dir = BASE_DIR/'mediafiles/profile/default.png'

    def __str__(self):
        return str(self.user.email)

    # def get_profile_pic_url(self):
    #     if self.profile_pic:
    #         return self.profile_pic.url
    #     return self.thumbnail_dir
