from ninja import NinjaAPI
from api.v1.categories.api import router as categories_router
from api.v1.tasks.api import router as tasks_router
from api.v1.users.api import router as users_router

api = NinjaAPI()

api.add_router("/categories/", categories_router)
api.add_router("/tasks/", tasks_router)
api.add_router("/users/", users_router)
