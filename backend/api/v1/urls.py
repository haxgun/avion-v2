from ninja_jwt.authentication import JWTAuth
from ninja_extra import NinjaExtraAPI

from api.v1.categories.api import router as categories_router
from api.v1.tasks.api import router as tasks_router
from api.v1.users.api import router as users_router

from api.v1.controller import CustomController

api = NinjaExtraAPI(
    title="Avion API",
    description="Simple but effective to-do list app aimed at modern design and ease of use.",
    auth=JWTAuth(),
)
api.register_controllers(CustomController)

api.add_router("/categories/", categories_router)
api.add_router("/tasks/", tasks_router)
api.add_router("/users/", users_router)
