from typing import List

from ninja import Router
from apps.categories.models import Category

from api.v1.categories.schema import CategoryOut, CategoryIn, NotFoundSchema

router = Router()


@router.post('/')
async def create_category(request, payload: CategoryIn) -> dict:
    category = await Category.objects.acreate(**payload.dict())
    return {'id': category.id}


@router.get('/', response=List[CategoryOut])
async def list_categories(request) -> list:
    return [category async for category in Category.objects.all()]


@router.get('/{category_id}', response=CategoryOut)
async def detail_category(request, category_id: int) -> dict:
    try:
        return await Category.objects.aget(id=category_id)
    except Category.DoesNotExist as e:
        return {'message': 'Category does not exist'}


@router.put('/{category_id}')
async def update_category(request, category_id: int, payload: CategoryIn) -> dict:
    try:
        category = await Category.objects.aget(id=category_id)
        for attribute, value in payload.dict().items():
            setattr(category, attribute, value)
        await category.asave()
        return {'success': True}
    except Category.DoesNotExist as e:
        return {'message': 'Category does not exist'}


@router.delete('/{category_id}')
async def delete_category(request, category_id: int) -> dict:
    try:
        category = await Category.objects.aget(id=category_id)
        await category.adelete()
        return {'success': True}
    except Category.DoesNotExist as e:
        return {'message': 'Task does not exist'}
