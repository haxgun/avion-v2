from typing import List

from ninja import Schema, ModelSchema
from pydantic import EmailStr

from apps.users.models import User
from api.v1.tasks.schema import TaskOut
from api.v1.categories.schema import CategoryOut


class UserOut(ModelSchema):
    tasks: List[TaskOut]
    categories: List[CategoryOut]

    class Config:
        model = User
        model_fields = ('id', 'nickname', 'email', 'last_login', 'date_joined', 'is_active')


class UserRegistrationInput(Schema):
    email: EmailStr
    nickname: str
    password: str


class UserRegistrationAndLoginOutput(Schema):
    id: int


class UserLoginInput(Schema):
    email: EmailStr
    password: str


class NotFoundSchema(Schema):
    message: str
