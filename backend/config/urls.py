from django.contrib import admin
from django.urls import path, include
from backend.api.v1.urls import api


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
]
