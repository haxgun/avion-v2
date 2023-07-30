from datetime import datetime
from typing import Optional

from ninja import Schema, ModelSchema
from apps.tasks.models import Tasks
from ninja.orm import create_schema


class TaskIn(ModelSchema):
    user_id: int
    category_id: Optional[int]
    due_date: Optional[datetime] = None

    class Config:
        model = Tasks
        model_fields = ('title', 'description', 'complete', 'creation_date', 'is_attached', 'priority',)


TaskOut = create_schema(Tasks)


class NotFoundSchema(Schema):
    message: str
