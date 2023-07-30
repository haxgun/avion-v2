from typing import Optional

from ninja import Schema, ModelSchema
from apps.categories.models import Category

from api.v1.users.schema import UserOut


class CategoryOut(ModelSchema):
    class Config:
        model = Category
        model_fields = '__all__'


class CategoryIn(ModelSchema):
    class Config:
        model = Category
        model_fields = '__all__'
        model_exclude = ('id',)


class NotFoundSchema(Schema):
    message: str
