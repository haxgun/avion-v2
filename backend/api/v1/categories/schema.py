from typing import Optional

from ninja import Schema, ModelSchema
from apps.categories.models import Category

from api.v1.users.schema import UserOut


class CategoryOut(ModelSchema):
    user: UserOut

    class Config:
        model = Category
        model_fields = ('id', 'title', 'description', 'color')


class CategoryIn(ModelSchema):
    user_id: int

    class Config:
        model = Category
        model_fields = ('title', 'description', 'color')


class NotFoundSchema(Schema):
    message: str
