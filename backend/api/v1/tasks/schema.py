from datetime import datetime

from ninja import Schema
from typing import Optional


class TasksSchema(Schema):
    user: Optional[int]
    title: str
    description: Optional[str]
    complete: bool
    creation_date: Optional[datetime]
    due_date: Optional[datetime]
    is_attached: bool
    category: Optional[int]
    priority: str


class NotFoundSchema(Schema):
    message: str
