from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import *


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=255, unique=True)
    mobile = models.CharField(max_length=13, null=True, blank=True, unique=True)
    is_mobile = models.BooleanField(default=False)
    is_email = models.BooleanField(default=False)
    key = models.TextField(max_length=20000, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['mobile', 'updated_at', 'is_mobile', 'is_email', 'key']
    objects = CustomUserManager()

    def _str_(self):
        return self.email

    class Meta:
        verbose_name_plural = "User"