from datetime import datetime

from ninja import Schema, ModelSchema
from typing import Optional

from apps.tasks.models import Tasks


class TasksSchema(ModelSchema):
    class Config:
        model = Tasks
        model_fields = ['user', 'title', 'description', 'complete', 'creation_date', 'due_date', 'is_attached', 'category', 'priority']


class NotFoundSchema(Schema):
    message: str
