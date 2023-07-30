from typing import List

from ninja import Router
from apps.users.models import User
from api.v1.users.schema import UserOut

router = Router()


@router.get("/", response=List[UserOut])
async def list_users(request) -> list:
    return [task async for task in User.objects.all()]
    # qs = User.objects.exclude(username='admin')
    # return qs


@router.get("/{user_id}", response=UserOut)
async def get_user(request, user_id: int) -> dict:
    try:
        return await User.objects.aget(id=user_id)
    except User.DoesNotExist as e:
        return {'message': 'User does not exist'}
