from typing import Optional

from ninja import Schema, ModelSchema
from apps.categories.models import Category

from api.v1.users.schema import UserOut


class CategoryOutF(Schema):
    id: int


class CategoryOut(Schema):
    id: int
    title: str
    description: Optional[str] = None
    user: UserOut
    color: str


class CategoryIn(Schema):
    title: str
    description: Optional[str] = None
    user: UserOut
    color: Optional[str] = '2196F3'


class NotFoundSchema(Schema):
    message: str
