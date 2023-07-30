from datetime import datetime
from typing import List

from ninja import Schema, ModelSchema

from apps.users.models import User
from api.v1.tasks.schema import TaskOut
from api.v1.categories.schema import CategoryOut


class UserOut(ModelSchema):
    tasks: List[TaskOut]
    categories: List[CategoryOut]

    class Config:
        model = User
        model_fields = ('id', 'nickname', 'email', 'last_login', 'date_joined', 'is_active')


class NotFoundSchema(Schema):
    message: str
