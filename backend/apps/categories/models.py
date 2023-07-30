from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=16384, null=True, blank=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='categories',
    )
    color = models.CharField(default='2196F3', max_length=7, blank=True)

    def __str__(self):
        return self.title
