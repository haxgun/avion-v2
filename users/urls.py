from django.urls import path

from users.api import api

app_name = "users"


urlpatterns = [
    path("users/", api.urls),
]
