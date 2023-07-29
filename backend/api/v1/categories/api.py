from typing import List

from ninja import Router
from apps.categories.models import Category

from api.v1.categories.schema import CategoriesSchema, NotFoundSchema

router = Router()


@router.get('/', response=List[CategoriesSchema])
def list_tasks(request):
    return Category.objects.all()


@router.get('/{category_id}', response={200: CategoriesSchema, 404: NotFoundSchema})
def detail_task(request, category_id: int):
    try:
        category = Category.objects.get(id=category_id)
        return category
    except Category.DoesNotExist as e:
        return 404, {"message": "Task does not exist"}


@router.post('/', response={201: CategoriesSchema})
def create_task(request, category: CategoriesSchema):
    category = Category.objects.create(**category.dict())
    return category


@router.put('/{category_id}', response={200: CategoriesSchema, 404: NotFoundSchema})
def update_task(request, category_id: int, data: CategoriesSchema):
    try:
        category = Category.objects.get(id=category_id)
        for attribute, value in data.dict().items():
            setattr(category, attribute, value)
        category.save()
        return 200, category
    except Category.DoesNotExist as e:
        return 404, {"message": "Task does not exist"}


@router.delete('/{category_id}', response={200: CategoriesSchema, 404: NotFoundSchema})
def delete_task(request, category_id: int):
    try:
        category = Category.objects.get(id=category_id)
        category.delete()
        return 200
    except Category.DoesNotExist as e:
        return 404, {"message": "Task does not exist"}

