from django.urls import path

from tasks.api import api

app_name = "tasks"


urlpatterns = [
    path("tasks/", api.urls),
]
