from datetime import datetime, date
from enum import Enum
from typing import Optional

from ninja import Schema, ModelSchema
from apps.tasks.models import Tasks

from api.v1.users.schema import UserOut, UserOutF
from api.v1.categories.schema import CategoryOut, CategoryOutF


class PriorityEnum(str, Enum):
    ahigh_priority = 'Высокий'
    bmedium_priority = 'Средний'
    clow_priority = 'Низкий'
    dlowest_priority = 'Самый низкий'
    edefault = 'Обычный'


class TaskIn(Schema):
    user_id: int
    title: str
    description: Optional[str] = ''
    complete: bool = False
    creation_date: datetime = date.today()
    due_date: Optional[datetime]
    is_attached: bool = False
    category: Optional[int]
    priority: PriorityEnum = PriorityEnum.edefault


class TaskOut(Schema):
    id: int
    user: UserOut
    title: str
    description: Optional[str] = ''
    complete: bool = False
    creation_date: datetime = date.today()
    due_date: Optional[datetime]
    is_attached: bool = False
    category: Optional[CategoryOut]
    priority: PriorityEnum


class NotFoundSchema(Schema):
    message: str
