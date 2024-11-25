from django.urls import path
from . import views


app_name = "catalog"

urlpatterns = [
    path("controller/", "controller", name="controller_name")
]
