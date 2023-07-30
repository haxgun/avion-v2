from django.contrib.auth import get_user_model
from django.db import models

from apps.categories.models import Category

User = get_user_model()


class Tasks(models.Model):
    PRIORITIES = (
        ('ahigh_priority', 'Высокий'),
        ('bmedium_priority', 'Средний'),
        ('clow_priority', 'Низкий'),
        ('dlowest_priority', 'Самый низкий'),
        ('edefault', 'Обычный')
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='tasks',
    )
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=16384, null=True, blank=True)
    complete = models.BooleanField(default=False, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    is_attached = models.BooleanField(default=False, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    priority = models.CharField(
        max_length=30,
        choices=PRIORITIES,
        default=PRIORITIES[-1][0],
        blank = True
    )

    def __str__(self):
        return self.title
