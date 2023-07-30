from datetime import datetime, date
from enum import Enum
from typing import Optional

from ninja import Schema, ModelSchema
from apps.tasks.models import Tasks

from api.v1.users.schema import UserOut
from api.v1.categories.schema import CategoryOut


class PriorityEnum(str, Enum):
    ahigh_priority = 'Высокий'
    bmedium_priority = 'Средний'
    clow_priority = 'Низкий'
    dlowest_priority = 'Самый низкий'
    edefault = 'Обычный'


class TaskIn(ModelSchema):
    user_id: int
    category_id: Optional[int]
    due_date: Optional[datetime] = None
    priority: PriorityEnum = PriorityEnum.edefault

    class Config:
        model = Tasks
        model_fields = ('title', 'description', 'complete', 'creation_date', 'is_attached',)


class TaskOut(Schema):
    user: UserOut
    category: Optional[CategoryOut]
    priority: PriorityEnum

    class Config:
        model = Tasks
        model_fields = ('id', 'title', 'description', 'complete', 'creation_date', 'due_date', 'is_attached')


class NotFoundSchema(Schema):
    message: str
