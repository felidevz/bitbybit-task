from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    TYPE_CHOICES = (
        ('S', 'Standard'),
        ('A', 'Admin'),
    )

    email = models.EmailField(verbose_name='email address', unique=True)
    type = models.CharField(max_length=1, default='S', choices=TYPE_CHOICES)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
