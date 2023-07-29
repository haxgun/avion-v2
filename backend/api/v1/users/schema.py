from datetime import datetime

from ninja import Schema


class UserSchema(Schema):
    id: int
    nickname: str
    email: str
    last_login: datetime
    date_join: datetime
    is_superuser: bool
    is_staff: bool
    is_active: bool


class NotFoundSchema(Schema):
    message: str
