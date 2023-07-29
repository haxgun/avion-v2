from typing import List

from ninja import Router
from apps.tasks.models import Tasks

from backend.api.v1.tasks.schema import TasksSchema, NotFoundSchema

router = Router()


@router.get('/', response={200: List[TasksSchema]})
def list_tasks(request):
    return Tasks.objects.all()
