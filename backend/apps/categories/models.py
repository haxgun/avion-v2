from django.contrib.auth import get_user_model
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=16384, null=True, blank=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    color = models.CharField(default='2196F3', max_length=7, blank=True)

    def __str__(self):
        return self.title
