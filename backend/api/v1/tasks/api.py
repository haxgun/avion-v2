from typing import List

from asgiref.sync import sync_to_async
from ninja import Router
from apps.tasks.models import Tasks

from api.v1.tasks.schema import TaskIn, TaskOut, NotFoundSchema

router = Router()


@router.post('/')
def create_task(request, payload: TaskIn) -> dict:
    task = Tasks.objects.create(**payload.dict())
    return {"id": task.id}


@router.get('/', response=List[TaskOut])
async def list_tasks(request) -> list:
    qs = Tasks.objects.select_related('user', 'category')
    return await sync_to_async(list)(qs)


@router.get('/{task_id}', response=TaskOut)
async def detail_task(request, task_id: int) -> dict:
    return await Tasks.objects.aget(pk=task_id)


@router.put('/{task_id}')
async def update_task(request, task_id: int, payload: TaskIn) -> dict:
    try:
        task = await Tasks.objects.aget(id=task_id)
        for attribute, value in payload.dict().items():
            setattr(task, attribute, value)
        await task.asave()
        return {"success": True}
    except Tasks.DoesNotExist as e:
        return {"message": "Task does not exist"}


@router.delete('/{task_id}')
async def delete_task(request, task_id: int) -> dict:
    try:
        task = await Tasks.objects.aget(id=task_id)
        await task.adelete()
        return {"success": True}
    except Tasks.DoesNotExist as e:
        return {"message": "Task does not exist"}

