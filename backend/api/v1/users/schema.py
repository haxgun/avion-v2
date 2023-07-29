from datetime import datetime

from ninja import Schema, ModelSchema

from apps.users.models import User


class UserOutF(Schema):
    id: int


class UserOut(ModelSchema):
    class Config:
        model = User
        model_fields = ('id', 'nickname', 'email', 'last_login', 'date_joined', 'is_active')


class NotFoundSchema(Schema):
    message: str
