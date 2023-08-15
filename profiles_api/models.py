from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in system"""
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10, unique=True)
    email = models.EmailField(max_length=255, null=True, blank=True)

    def __str__(self):
        """Returns user field"""
        return self.phone_number
