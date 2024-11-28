from django.urls import path
from . import views
from catalog.apps import CatalogConfig


app_name = CatalogConfig.name

urlpatterns = [
    path("home_page/", views.home_page, name="home_page"),
    path("contacts/", views.contacts, name="contacts"),
]
