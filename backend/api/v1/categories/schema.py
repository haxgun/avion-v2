from ninja import Schema, ModelSchema
from apps.categories.models import Category
from ninja.orm import create_schema

CategoryOut = create_schema(Category)


class CategoryIn(ModelSchema):
    user_id: int

    class Config:
        model = Category
        model_fields = ('title', 'description', 'color',)


class NotFoundSchema(Schema):
    message: str
