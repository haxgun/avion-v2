from typing import List

from django.contrib.auth import login, authenticate
from ninja import Router
from apps.users.models import User
from api.v1.users.schema import UserOut, NotFoundSchema, UserRegistrationInput, UserLoginInput, UserRegistrationAndLoginOutput

router = Router()


@router.get('/', response=List[UserOut])
async def list_users(request) -> list:
    return [task async for task in User.objects.all()]


@router.get('/{user_id}', response={200: UserOut, 404: NotFoundSchema})
async def get_user(request, user_id: int) -> dict:
    try:
        return 200, await User.objects.aget(id=user_id)
    except User.DoesNotExist as e:
        return 404, {'message': 'User does not exist'}


@router.post('/register/', response={200: UserRegistrationAndLoginOutput, 404: NotFoundSchema}, auth=None)
async def register_user(request, payload: UserRegistrationInput) -> dict:
    if not User.objects.filter(email=payload.email).exists():
        user = User.objects.create_user(**payload.dict())
        if user:
            login(request, user)
            return 200, {'id': user.id}
    return 404, {'message': 'Username already exists'}


@router.post('/login/', response={200: UserRegistrationAndLoginOutput, 402: NotFoundSchema}, auth=None)
async def login_user(request, payload: UserLoginInput) -> dict:
    user = authenticate(**payload.dict())
    if user:
        login(request, user)
        return 200, {'id': user.id}
    return 404, {'message': 'Invalid credentials'}
