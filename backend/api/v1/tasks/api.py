from typing import List

from ninja import Router
from apps.tasks.models import Tasks

from api.v1.tasks.schema import TasksSchema, NotFoundSchema

router = Router()


@router.get('/', response=List[TasksSchema])
def list_tasks(request):
    return Tasks.objects.all()


@router.get('/{task_id}', response={200: TasksSchema, 404: NotFoundSchema})
def detail_task(request, task_id: int):
    try:
        task = Tasks.objects.get(id=task_id)
        return task
    except Tasks.DoesNotExist as e:
        return 404, {"message": "Task does not exist"}


@router.post('/', response={201: TasksSchema})
def create_task(request, task: TasksSchema):
    task = Tasks.objects.create(**task.dict())
    return task


@router.put('/{task_id}', response={200: TasksSchema, 404: NotFoundSchema})
def update_task(request, task_id: int, data: TasksSchema):
    try:
        task = Tasks.objects.get(id=task_id)
        for attribute, value in data.dict().items():
            setattr(task, attribute, value)
        task.save()
        return 200, task
    except Tasks.DoesNotExist as e:
        return 404, {"message": "Task does not exist"}


@router.delete('/{task_id}', response={200: TasksSchema, 404: NotFoundSchema})
def delete_task(request, task_id: int):
    try:
        task = Tasks.objects.get(id=task_id)
        task.delete()
        return 200
    except Tasks.DoesNotExist as e:
        return 404, {"message": "Task does not exist"}

