from django.db import models
from django.contrib.auth.models import AbstractUser
from homesapp.models import Property
from django.conf import settings

# Create your models here.


class UserInfo(AbstractUser):
    is_agent = models.BooleanField(default=False)
    favorite = models.ManyToManyField(Property, blank=True, related_name='user_favourite')

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_zip = models.CharField(max_length=10, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username
