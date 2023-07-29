from ninja import Schema, ModelSchema
from apps.categories.models import Category


class CategoriesSchema(ModelSchema):
    class Config:
        model = Category
        model_fields = ['id', 'title', 'description', 'user', 'color']


class NotFoundSchema(Schema):
    message: str
