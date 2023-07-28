from django.urls import path

from categories.api import api

app_name = "categories"


urlpatterns = [
    path("categories/", api.urls),
]
