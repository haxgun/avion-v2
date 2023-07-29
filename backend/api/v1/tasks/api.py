from typing import List

from ninja import Router
from apps.tasks.models import Tasks

from api.v1.tasks.schema import TaskIn, TaskOut, NotFoundSchema

router = Router()


@router.post('/')
async def create_task(request, payload: TaskIn) -> dict:
    task = await Tasks.objects.acreate(**payload.dict())
    return {'id': task.id}


@router.get('/', response=List[TaskOut])
async def list_tasks(request) -> list:
    return [task async for task in Tasks.objects.all()]


@router.get('/{task_id}', response=TaskOut)
async def detail_task(request, task_id: int) -> dict:
    try:
        return await Tasks.objects.aget(id=task_id)
    except Tasks.DoesNotExist as e:
        return {'message': 'Task does not exist'}


@router.put('/{task_id}')
async def update_task(request, task_id: int, payload: TaskIn) -> dict:
    try:
        task = await Tasks.objects.aget(id=task_id)
        for attribute, value in payload.dict().items():
            setattr(task, attribute, value)
        await task.asave()
        return {'success': True}
    except Tasks.DoesNotExist as e:
        return {'message': 'Task does not exist'}


@router.delete('/{task_id}')
async def delete_task(request, task_id: int) -> dict:
    try:
        task = await Tasks.objects.aget(id=task_id)
        await task.adelete()
        return {'success': True}
    except Tasks.DoesNotExist as e:
        return {'message': 'Task does not exist'}
