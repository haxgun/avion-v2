from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from apps.users.managers import CustomUserManager


class User(AbstractUser):
    username = None
    first_name = None
    last_name = None

    nickname = models.CharField(default='Без имени', max_length=32, blank=False, null=False)
    email = models.EmailField(_('email address'), unique=True, blank=None, null=None)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']
    objects = CustomUserManager()

    def __str__(self):
        return self.email
