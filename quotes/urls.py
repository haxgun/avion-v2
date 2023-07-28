from django.urls import path

from quotes.api import api

app_name = "quotes"


urlpatterns = [
    path("quotes/", api.urls),
]
